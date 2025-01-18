def evaluate_company(score):
    """
    Evaluate a company's score and return a rank.
    """
    try:
        score = float(score)  # Convert score to a number
        if score >= 800:
            return 'A'
        elif score >= 500:
            return 'B'
        elif score >= 200:
            return 'C'
        else:
            return 'D'
    except ValueError:
        return 'N/A'  # Return N/A for invalid scores
