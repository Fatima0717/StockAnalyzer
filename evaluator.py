def evaluate_stock(data, popularity, sector_growth, shikiho_data):
    """
    Extended evaluation logic
    """
    score = 0
    details = []

    # 1. Popularity score
    if popularity > 50:
        score += 20
        details.append("High popularity (Score +20)")
    elif popularity > 20:
        score += 10
        details.append("Moderate popularity (Score +10)")
    else:
        details.append("Low popularity (Score +0)")

    # 2. Industry growth rate
    if sector_growth > 5:
        score += 20
        details.append("Industry is growing (Score +20)")
    elif sector_growth > 2:
        score += 10
        details.append("Industry is stable (Score +10)")
    else:
        details.append("Low industry growth (Score +0)")

    # 3. Shikiho data
    if shikiho_data:
        growth = shikiho_data.get("growth", 0)
        profit_margin = shikiho_data.get("profit_margin", 0)

        if growth > 10:
            score += 20
            details.append("High growth rate (Score +20)")
        if profit_margin > 5:
            score += 10
            details.append("High profit margin (Score +10)")

    # Ranking
    rank = "A" if score >= 70 else "B" if score >= 50 else "C"
    return {"score": score, "rank": rank, "details": details}