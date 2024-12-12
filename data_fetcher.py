import requests
import yfinance as yf
from bs4 import BeautifulSoup

def get_shikiho_data(company_name):
    """
    Scrape and obtain Shikiho data (hypothetical example).
    """
    try:
        # Incorporate the company name into the URL (example for Toyo Keizai site)
        url = f"https://shikiho.toyokeizai.net/us/{company_name.replace(' ', '+')}"
        response = requests.get(url)

        # Check HTTP status code
        if response.status_code != 200:
            print(f"Failed to obtain Shikiho data: HTTP {response.status_code}")
            return None

        # Parse HTML with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Save HTML for debugging
        with open("shikiho_debug.html", "w", encoding="utf-8") as f:
            f.write(soup.prettify())

        # Extract necessary data
        growth = soup.find("div", {"id": "growth"})
        profit_margin = soup.find("div", {"id": "profit_margin"})

        # Check for None
        if not growth:
            print(f"Growth rate for '{company_name}' not found.")
        if not profit_margin:
            print(f"Profit margin for '{company_name}' not found.")

        if not profit_margin:
            print(f"Profit margin for '{company_name}' not found.")
            return None

    except Exception as e:
        print(f"Error obtaining Shikiho data: {e}")
        return None

def get_stock_data(ticker):
    """
    Obtain basic stock information.
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
        print(f"Error obtaining stock data: {e}")
        return None
    
if __name__ == "__main__":
    company_name = "Consolidated Edison"
    print(f"Obtaining Shikiho data for '{company_name}'...")

    shikiho_data = get_shikiho_data(company_name)
    if shikiho_data:
        print("Obtained Shikiho data:")
        for key, value in shikiho_data.items():
            print(f"{key}: {value}")
    else:
        print("Failed to obtain Shikiho data.")