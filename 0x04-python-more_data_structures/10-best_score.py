#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return
    winner = None
    winner_score = 0
    for k, v in a_dictionary.items():
        if v > winner_score:
            winner = k
            winner_score = v
    return winner
