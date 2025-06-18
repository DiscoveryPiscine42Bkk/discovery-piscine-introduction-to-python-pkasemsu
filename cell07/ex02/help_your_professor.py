def average(score_dict):
    if not score_dict:
        return 0  # Avoid division by zero
    total = sum(score_dict.values())
    count = len(score_dict)
    return total / count

if __name__ == "__main__":
    scores = {
        "Alice": 85,
        "Bob": 90,
        "Charlie": 78,
        "Daisy": 92
    }

    avg = average(scores)
    print("Class average:", avg)