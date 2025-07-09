import random

def player(prev_play, opponent_history=[]):
    # Save opponent history
    if prev_play:
        opponent_history.append(prev_play)

    # First move
    if len(opponent_history) == 0:
        return random.choice(["R", "P", "S"])

    # Move that beats a given move
    counter = {"R": "P", "P": "S", "S": "R"}

    # --- Strategy 1: Frequency Counter (beats quincy & mrugesh) ---
    freq = {"R": 0, "P": 0, "S": 0}
    for move in opponent_history:
        freq[move] += 1

    most_common = max(freq, key=freq.get)

    # --- Strategy 2: Pattern Prediction (beats abbey & kris) ---
    if len(opponent_history) >= 3:
        last_two = "".join(opponent_history[-2:])
        patterns = {}

        for i in range(len(opponent_history) - 2):
            seq = opponent_history[i] + opponent_history[i + 1]
            next_move = opponent_history[i + 2]
            if seq == last_two:
                patterns[next_move] = patterns.get(next_move, 0) + 1

        if patterns:
            predicted = max(patterns, key=patterns.get)
            return counter[predicted]

    # --- Mixed Strategy ---
    # Mostly play counter to most common, sometimes random
    if random.random() < 0.8:
        return counter[most_common]
    else:
        return random.choice(["R", "P", "S"])

