from data_fetcher import get_stock_data, get_popularity, get_sector_growth, get_shikiho_data
from evaluator import evaluate_stock

while True:
    ticker = input("ティッカーシンボルを入力してください（例：ED) :")
    data = get_stock_data(ticker)
    
    if data:
        # 基本情報を表示
        print("\n取得したデータ:")
        for key, value in data.items():
            print(f"{key}: {value}")
        
        # 人気度を取得
        company_name = data.get("name", ticker)  # 企業名がなければティッカーを利用
        popularity = get_popularity(company_name)
        print(f"\n人気度: {popularity}")

        # 業界成長率を取得
        sector = data.get("sector", "Unknown")
        sector_growth = get_sector_growth(sector)
        print(f"業界（{sector}）の成長率: {sector_growth}%")

        # 四季報データを取得
        shikiho_data = get_shikiho_data(company_name)
        if shikiho_data:
            print("\n四季報データ:")
            for key, value in shikiho_data.items():
                print(f"{key}: {value}")
        else:
            print("\n四季報データを取得できませんでした。")

        # 評価ロジックを実行
        print("\n評価結果:")
        result = evaluate_stock(data, popularity, sector_growth, shikiho_data)
        print(f"スコア: {result['score']}")
        print(f"ランク: {result['rank']}")
        print("詳細:")
        for detail in result["details"]:
            print(f" - {detail}")
        
        break # ループを終了
    else:
        print("無効なティッカーシンボルです。再度入力してください。")
    
    # エラー処理
    if not data:
        print("無効なティッカーシンボルです。再度入力してください。")
