
import os
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel, Field
from google.genai import types


# 讀取環境變數
load_dotenv()


# 定義 AI 分析報告格式
class StockAnalysis(BaseModel):
    trend: str = Field(description="近期股價趨勢分析")
    price_analysis: str = Field(description="近期價格變化分析")
    risk_analysis: str = Field(description="可能的市場風險")
    summary: str = Field(description="股票綜合摘要")


def analyze_stock(stock_id, data):

    # 取得 API 金鑰
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("找不到 Gemini API 金鑰，請檢查 .env 檔案。")
        return

    # 建立 Gemini 客戶端
    client = genai.Client(api_key=api_key)

    # 整理最近十筆股票資料
    recent_data = data.tail(10)[
        ["Open", "High", "Low", "Close", "Volume"]
    ].round(2).to_string()

    # 建立分析提示詞
    prompt = f"""
    你是一位股票資料分析助理。

    請根據以下真實歷史資料，
    分析台灣股票 {stock_id}。

    最近十筆股票資料：
    {recent_data}

    請注意：
    1. 只能根據提供的資料進行分析。
    2. 不可以編造股價或市場消息。
    3. 說明近期價格變化。
    4. 提醒使用者可能的投資風險。
    5. 不可以保證未來股價漲跌。
    6. 如果資料不足，請明確說明。
    """

    print("\n========== Gemini AI 股票分析 ==========")
    print("AI 正在分析，以下為串流輸出：\n")

    try:
        # 使用 Structured Output + Streaming
        response_stream = client.models.generate_content_stream(
            model="gemini-flash-latest",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_json_schema=StockAnalysis.model_json_schema()
            )
        )

        # 接收串流內容
        full_response = ""

        for chunk in response_stream:
            if chunk.text:
                print(chunk.text, end="", flush=True)
                full_response += chunk.text

        print("\n\n========== AI 分析報告 ==========")

        # 驗證 AI 是否符合指定格式
        result = StockAnalysis.model_validate_json(full_response)

        print("\n【股價趨勢】")
        print(result.trend)

        print("\n【價格分析】")
        print(result.price_analysis)

        print("\n【風險分析】")
        print(result.risk_analysis)

        print("\n【綜合摘要】")
        print(result.summary)
        
        return result.model_dump()

    except Exception as e:
        print("\nGemini AI 分析發生錯誤：", e)
