# Example file for Advanced Python by Joe Marini
# Itertools: combinations and permutations

import itertools


# product() produces the cartesian product of input iterables
""""
52 cards
[('A', 'S'), ('A', 'C'), ('A', 'H'), ('A', 'D'), ('2', 'S'), ('2', 'C'), ('2', 'H'), ('2', 'D'), 
('3', 'S'), ('3', 'C'), ('3', 'H'), ('3', 'D'), ('4', 'S'), ('4', 'C'), ('4', 'H'), ('4', 'D'), 
('5', 'S'), ('5', 'C'), ('5', 'H'), ('5', 'D'), ('6', 'S'), ('6', 'C'), ('6', 'H'), ('6', 'D'), 
('7', 'S'), ('7', 'C'), ('7', 'H'), ('7', 'D'), ('8', 'S'), ('8', 'C'), ('8', 'H'), ('8', 'D'), 
('9', 'S'), ('9', 'C'), ('9', 'H'), ('9', 'D'), ('T', 'S'), ('T', 'C'), ('T', 'H'), ('T', 'D'), 
('J', 'S'), ('J', 'C'), ('J', 'H'), ('J', 'D'), ('Q', 'S'), ('Q', 'C'), ('Q', 'H'), ('Q', 'D'), 
('K', 'S'), ('K', 'C'), ('K', 'H'), ('K', 'D')]
"""
cards = "A23456789TJQK"
suits = "SCHD"

deck = list(itertools.product(cards, suits))
print(len(deck), "cards")
print(deck)

# permutations() creates tuples of a given length with no repeated elements
# priklad 4 tymy a kazdy hraje s kazdym, turnajovy mod 
"""
[('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'A'), ('B', 'C'), ('B', 'D'), 
('C', 'A'), ('C', 'B'), ('C', 'D'), ('D', 'A'), ('D', 'B'), ('D', 'C')]
"""
teams = ("A","B","C","D")
result = itertools.permutations(teams, 2)
print(list(result))

# combinations() will create combinations of a given length with no repeats
# ako permutace ale npovoluje stejne vysledky jako A vs B je stejne jako B vs A
# na poradi zde nezalezi
"""
[('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
"""
result = itertools.combinations(teams, 2)
print(list(result))


# combinations_with_replacement() will create combinations of a given length with repeats
# mame zde opakujici se elemnty jako A vs A nebo B vs B
"""
[('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'B'), 
('B', 'C'), ('B', 'D'), ('C', 'C'), ('C', 'D'), ('D', 'D')]
"""
result = itertools.combinations_with_replacement(teams, 2)
print(list(result))