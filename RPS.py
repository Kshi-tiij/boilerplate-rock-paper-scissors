import random
from collections import Counter

# Track bot-specific strategies
bot_counter = {"quincy": 0, "mrugesh": 0, "kris": 0, "abbey": 0}


def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    if not opponent_history:
        return random.choice(["R", "P", "S"])  # First random move

    counter = {"R": "P", "P": "S", "S": "R"}

    # Quincy Strategy: Predict based on cycle
    quincy_pattern = ["R", "R", "P", "P", "S"]
    if len(opponent_history) <= 5:
        predicted_quincy = quincy_pattern[len(opponent_history) % len(quincy_pattern)]
        return counter[predicted_quincy]

    # Mrugesh Strategy: Counter most frequent in the last 10 moves
    if len(opponent_history) >= 10:
        last_ten = opponent_history[-10:]
        most_common = Counter(last_ten).most_common(1)[0][0]
        return counter[most_common]

    # Kris Strategy: Counter the previous opponent move
    if len(opponent_history) > 0:
        return counter[opponent_history[-1]]

    # Abbey Strategy: Pattern recognition
    if len(opponent_history) >= 2:
        last_two = "".join(opponent_history[-2:])
        patterns = {
            "RR": "P", "RP": "S", "RS": "P",
            "PR": "S", "PP": "R", "PS": "S",
            "SR": "P", "SP": "R", "SS": "R"
        }
        if last_two in patterns:
            return patterns[last_two]

    # Fallback: Random to prevent predictability
    return random.choice(["R", "P", "S"])
