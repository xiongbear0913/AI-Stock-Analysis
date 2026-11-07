
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from ai_analysis import analyze_stock
import json
from stock_utils import is_valid_stock_id

def plot_stock_chart(data, stock_id):
    """繪製股票價格與成交量圖表"""

    # 設定中文字體
    plt.rcParams["font.sans-serif"] = [
        "Microsoft JhengHei",
        "Arial"
    ]
    plt.rcParams["axes.unicode_minus"] = False

    # 建立上下兩個圖表
    fig, (ax1, ax2) = plt.subplots(
        2,
        1,
        figsize=(12, 8),
        sharex=True,
        gridspec_kw={"height_ratios": [3, 1]}
    )

    # 第一張：收盤價走勢
    ax1.plot(
        data.index,
        data["Close"],
        label="每日收盤價",
        linewidth=2
    )

    ax1.set_title(
        f"{stock_id} 股票價格走勢圖",
        fontsize=16
    )
    ax1.set_ylabel("價格（元）")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # 第二張：成交量
    ax2.bar(
        data.index,
        data["Volume"],
        label="每日成交量"
    )

    ax2.set_ylabel("成交量")
    ax2.set_xlabel("日期")
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    # 日期格式
    ax2.xaxis.set_major_formatter(
        mdates.DateFormatter("%Y-%m-%d")
    )

    fig.autofmt_xdate()
    plt.tight_layout()

    # 顯示圖表
    plt.show()

def get_stock_data(stock_id):
    """取得台灣股票歷史資料"""

    # 台灣上市股票代號
    ticker = stock_id + ".TW"

    print("\n正在查詢股票資料，請稍候...")

    try:
        stock = yf.Ticker(ticker)

        # 取得最近三個月的日線資料
        data = stock.history(
            period="3mo",
            interval="1d",
            auto_adjust=False
        )

        # 檢查是否有取得資料
        if data.empty:
            print("查無股票資料，請確認股票代號。")
            return

        # 取得最近兩筆收盤價
        latest = data.iloc[-1]
        previous = data.iloc[-2] if len(data) >= 2 else None

        latest_close = latest["Close"]

        print("\n========== 股票查詢結果 ==========")
        print(f"股票代號：{stock_id}")
        print(f"股票名稱：{stock_id}（台灣上市股票）")
        print(f"資料日期：{data.index[-1].strftime('%Y-%m-%d')}")
        print(f"最近收盤價：{latest_close:.2f} 元")

        if previous is not None:
            previous_close = previous["Close"]
            change = latest_close - previous_close
            change_percent = change / previous_close * 100

            print(f"前一筆收盤價：{previous_close:.2f} 元")
            print(f"漲跌金額：{change:+.2f} 元")
            print(f"漲跌幅：{change_percent:+.2f}%")

        print(f"三個月最高價：{data['High'].max():.2f} 元")
        print(f"三個月最低價：{data['Low'].min():.2f} 元")

        print("\n========== 最近五筆歷史資料 ==========")

        print(
            data[["Open", "High", "Low", "Close", "Volume"]]
            .tail()
            .round(2)
            .to_string()
        )

        print("\n股票資料查詢完成！")

        # 呼叫 Gemini AI 分析
        analysis_result = analyze_stock(stock_id, data)

        # 儲存分析結果到 JSON
        if analysis_result:
            output_data = {
                "stock_id": stock_id,
                "analysis": analysis_result
                }
            with open("docs/analysis.json", "w", encoding="utf-8") as file:
                json.dump(
                    output_data,
                    file,
                    ensure_ascii=False,
                    indent=4
                    )
                print("AI 分析結果已儲存至 docs/analysis.json")
        else:
            print("AI 分析未成功，沒有產生 JSON 檔案。")

        # 顯示股價走勢圖
        plot_stock_chart(data, stock_id)

    except Exception as e:
        print("查詢過程發生錯誤：", e)


def main():
    print("==============================")
    print("       AI 智慧股票分析系統")
    print("==============================")

    print("目前支援：台灣上市股票")

    stock_id = input("\n請輸入股票代號（例如 2330）：").strip()

    if not is_valid_stock_id(stock_id):
        print("股票代號格式不正確，請輸入 4 至 6 位數字。")
        return

    get_stock_data(stock_id)


if __name__ == "__main__":
    main()
