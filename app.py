import pandas as pd

def main():
    # create sample data
    data = {
        'Company': ['Company A', 'Company B', 'Company C'],
        'Price': [100, 200, 300]
    }
    df = pd.DataFrame(data)
    
    # Display data
    print("Stock Data:")
    print(df)

if __name__ == "__main__":
    main()