import pandas as pd
import yfinance as yf
from evaluator import evaluate_company

def get_stock_price(ticker):
    """
    Fetch the current stock price for the given ticker symbol.
    """
    try:
        stock = yf.Ticker(ticker)
        stock_info = stock.info
        return stock_info.get("currentPrice", "N/A")
    except Exception as e:
        print(f"Error obtaining stock price for {ticker}: {e}")
        return "N/A"

def main():
    # Define the companies and their ticker symbols
    companies = {
        'Tesla': 'TSLA',
        'Microsoft': 'MSFT',
        'Toyota': 'TM',
        'Nestlé': 'NESN.SW',
        'Coca-Cola': 'KO'
    }
    
    # Fetch stock prices
    data = {
        'Company': [],
        'Price': [],
        'Score': [],
        'Rank': []
    }
    
    for company, ticker in companies.items():
        price = get_stock_price(ticker)
        score = price  # Assuming score is based on price for simplicity
        rank = evaluate_company(score)
        
        data['Company'].append(company)
        data['Price'].append(price)
        data['Score'].append(score)
        data['Rank'].append(rank)
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Display data
    print("Stock Data:")
    print(df)

if __name__ == "__main__":
    main()