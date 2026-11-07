# AI 智慧股票分析系統

## 一、專案介紹
本專案使用 Python 開發，提供台灣股票歷史資料查詢與 AI 分析功能。

使用者輸入股票代號後，系統會取得歷史股價資料，並透過 Gemini AI 產生分析內容。

本系統僅供學習與歷史資料分析，不構成投資建議。

## 二、功能特色
- 查詢台灣上市股票歷史資料
- 顯示近期收盤價與價格變化
- 使用 Matplotlib 繪製股價圖表
- 使用 Gemini AI 分析股票趨勢
- 使用 Structured Output 整理 AI 分析結果
- 使用 Streaming 接收 AI 回應
- 將分析結果儲存為 JSON
- 使用 GitHub Pages 展示專案成果

## 三、使用技術
- Python
- yfinance
- Pandas
- Matplotlib
- Google Gemini API
- Pydantic
- HTML
- CSS
- JavaScript
- GitHub Actions
- GitHub Pages

## 四、如何執行

### 環境需求
- Python 3.11 或以上版本
- uv 套件管理工具
- Gemini API Key

### 安裝與設定

1. 安裝 Python 與 uv。
2. 在專案根目錄建立 `.env` 檔案。
3. 在 `.env` 設定 Gemini API Key：

```env
GEMINI_API_KEY=你的_API_KEY
```

4. 開啟終端機，輸入以下指令安裝套件：

```bash
uv sync
```

5. 執行 Python 程式：

```bash
uv run main.py
```

6. 輸入台灣上市股票代號，例如 2330。
7. 等待系統取得歷史股價資料並進行 AI 分析。

注意：
- Gemini API 可能因服務負載而暫時無法回應。
- 請勿將 `.env` 或 API Key 上傳至 GitHub。

## 五、執行結果
系統可以顯示股票歷史資料、股價圖表，以及 AI 分析結果。

網站目前使用範例 JSON 展示分析版面；範例資料不代表即時 AI 分析結果。

## 六、AI 使用說明
本專案使用 Google Gemini API 協助分析股票資料。

使用的 AI 技術：
- Streaming：逐步接收 AI 回應。
- Structured Output：將 AI 分析整理成固定欄位。

AI 分析欄位包含：
- 近期趨勢
- 價格分析
- 風險分析
- 綜合摘要

開發者負責撰寫 Python 程式、設計網頁、檢查分析結果與調整程式內容。

## 七、注意事項
- 請勿將 `.env` 或 API Key 上傳至 GitHub。
- 股票資料可能有延遲或缺漏。
- 本系統僅供學習用途，不構成投資建議。