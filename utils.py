def calculate_score(levels):

    total = sum(levels.values())

    if total == 0:
        return 0

    score = (
        levels.get("Focused", 0) * 100 +
        levels.get("Distracted", 0) * 50 +
        levels.get("Drowsy", 0) * 20 +
        levels.get("Sleeping", 0) * 0
    ) / total

    return max(0, min(100, int(score)))