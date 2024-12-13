from data_fetcher import get_stock_data, get_popularity, get_sector_growth, get_shikiho_data
from evaluator import evaluate_stock
from shikiho_parser import parse_shikiho_html

while True:
    ticker = input("Please enter the ticker symbol (e.g., ED): ")
    data = get_stock_data(ticker)
    
    if data:
        # Display basic information
        print("\nRetrieved data:")
        for key, value in data.items():
            print(f"{key}: {value}")
        
        # Get popularity
        company_name = data.get("name", ticker)  # Use ticker if company name is not available
        popularity = get_popularity(company_name)
        print(f"\nPopularity: {popularity}")

        # Get industry growth rate
        sector = data.get("sector", "Unknown")
        sector_growth = get_sector_growth(sector)
        print(f"Industry ({sector}) growth rate: {sector_growth}%")

        # Get Shikiho data
        shikiho_html = get_shikiho_data(company_name)
        if shikiho_html:
            shikiho_data = parse_shikiho_html(shikiho_html)
            print("\nShikiho data:")
            for key, value in shikiho_data.items():
                print(f"{key}: {value}")
        else:
            print("\nFailed to retrieve Shikiho data.")

        # Execute evaluation logic
        print("\nEvaluation result:")
        result = evaluate_stock(data, popularity, sector_growth, shikiho_data)
        print(f"Score: {result['score']}")
        print(f"Rank: {result['rank']}")
        print("Details:")
        for detail in result["details"]:
            print(f" - {detail}")
        
        break # Exit the loop
    else:
        print("Invalid ticker symbol. Please try again.")
    
    # Error handling
    if not data:
        print("Invalid ticker symbol. Please try again.")