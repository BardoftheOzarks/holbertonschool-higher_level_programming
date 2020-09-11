#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best_score = 0
    for name, score in a_dictionary.items():
        if score > best_score:
            best = name
            best_score = score
    return best
