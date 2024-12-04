def evaluate_stock(data, popularity, sector_growth, shikiho_data):
    """
    拡張評価ロジック
    """
    score = 0
    details = []

    # 1. 人気度スコア
    if popularity > 50:
        score += 20
        details.append("人気度が高い（スコア+20）")
    elif popularity > 20:
        score += 10
        details.append("人気度が中程度（スコア+10）")
    else:
        details.append("人気度が低い（スコア+0）")

    # 2. 業界成長率
    if sector_growth > 5:
        score += 20
        details.append("業界が成長中（スコア+20）")
    elif sector_growth > 2:
        score += 10
        details.append("業界が安定（スコア+10）")
    else:
        details.append("業界成長が低い（スコア+0）")

    # 3. 四季報データ
    if shikiho_data:
        growth = shikiho_data.get("growth", 0)
        profit_margin = shikiho_data.get("profit_margin", 0)

        if growth > 10:
            score += 20
            details.append("高い成長率（スコア+20）")
        if profit_margin > 5:
            score += 10
            details.append("利益率が高い（スコア+10）")

    # ランク付け
    rank = "A" if score >= 70 else "B" if score >= 50 else "C"
    return {"score": score, "rank": rank, "details": details}
