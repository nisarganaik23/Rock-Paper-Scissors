import random

def quincy(prev_play, _=[]):
    return ["R", "P", "S"][len(prev_play) % 3]

def play(player1, player2, num_games=1000, verbose=False):
    player1_history = []
    player2_history = []
    player1_wins = 0
    player2_wins = 0

    for _ in range(num_games):
        move1 = player1(player2_history[-1] if player2_history else "")
        move2 = player2(player1_history[-1] if player1_history else "")
        player1_history.append(move1)
        player2_history.append(move2)

        if verbose:
            print(f"Player 1: {move1} | Player 2: {move2}")

        if move1 == "R" and move2 == "S" or move1 == "P" and move2 == "R" or move1 == "S" and move2 == "P":
            player1_wins += 1
        elif move2 == "R" and move1 == "S" or move2 == "P" and move1 == "R" or move2 == "S" and move1 == "P":
            player2_wins += 1

    print(f"Player 1 Wins: {player1_wins}")
    print(f"Player 2 Wins: {player2_wins}")
    print(f"Ties: {num_games - player1_wins - player2_wins}")
