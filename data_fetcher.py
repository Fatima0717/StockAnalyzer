import requests
import yfinance as yf
from bs4 import BeautifulSoup

def get_shikiho_data(company_name):
    """
    四季報データをスクレイピングして取得します（仮想例）。
    """
    try:
        # 実際に会社名をURLに組み込む方法（例としてトヨケイサイト）
        url = f"https://shikiho.toyokeizai.net/us/{company_name.replace(' ', '+')}"
        response = requests.get(url)

        # HTTPステータスコードの確認
        if response.status_code != 200:
            print(f"四季報データ取得失敗: HTTP {response.status_code}")
            return None

        # BeautifulSoupでHTML解析
        soup = BeautifulSoup(response.text, 'html.parser')

        # デバッグ用にHTML保存
        with open("shikiho_debug.html", "w", encoding="utf-8") as f:
            f.write(soup.prettify())

        # 必要なデータを抽出
        growth = soup.find("div", {"id": "growth"})
        profit_margin = soup.find("div", {"id": "profit_margin"})

        # Noneチェック
        if not growth:
            print(f"'{company_name}' の成長率が見つかりませんでした。")
        if not profit_margin:
            print(f"'{company_name}' の利益率が見つかりませんでした。")

        if not profit_margin:
            print(f"'{company_name}' の利益率が見つかりませんでした。")
            return None

    except Exception as e:
        print(f"四季報データ取得中にエラー: {e}")
        return None

def get_stock_data(ticker):
    """
    株の基本的な情報を取得します。
    """
    try:
        stock = yf.Ticker(ticker)
        stock_info = stock.info
        return {
            "name": stock_info.get("longName", "M/A"),
            "sector": stock_info.get("sector", "N/A"),
            "price": stock_info.get("currentPrice", "N/A")
        }
    except Exception as e:
        print(f"株データ取得中にエラー：{e}")
        return None
    
if __name__ == "__main__":
    company_name = "Consolidated Edison"
    print(f"'{company_name}' の四季報データを取得します...")

    shikiho_data = get_shikiho_data(company_name)
    if shikiho_data:
        print("取得した四季報データ:")
        for key, value in shikiho_data.items():
            print(f"{key}: {value}")
    else:
        print("四季報データを取得できませんでした。")
