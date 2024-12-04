import pandas as pd

def main():
    # サンプルデータを作成
    data = {
        'Company': ['Company A', 'Company B', 'Company C'],
        'Price': [100, 200, 300]
    }
    df = pd.DataFrame(data)
    
    # データを表示
    print("Stock Data:")
    print(df)

if __name__ == "__main__":
    main()