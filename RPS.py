def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    if opponent_history:
        most_common = max(set(opponent_history), key=opponent_history.count)
        counters = {"R": "P", "P": "S", "S": "R"}
        return counters[most_common]
    else:
        return "R"
