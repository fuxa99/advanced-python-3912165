# Example file for Advanced Python by Joe Marini
# Itertools: count, cycle, accumulate


import itertools

names = ["Joe", "Jane", "Jim"]

# cycle iterator can be used to cycle over a collection infinitely
"""
Joe
Jane
Jim
Joe - znova iteruje odznova
"""
cycler = itertools.cycle(names)
print(next(cycler))
print(next(cycler))
print(next(cycler))
print(next(cycler))

# use count to create a simple counter
"""
100
110
120 - iteruje promenou, fajn jelikoz neni potreba mit nejakou globalni promenou
"""
counter = itertools.count(100,10)
print(next(counter))
print(next(counter))
print(next(counter))

# accumulate creates an iterator that accumulates values
"""
[10, 30, 60, 100, 150, 190, 220]
  10+20 30+30
  dela sumaci s predchozi hodnotou 
"""
vals = [10,20,30,40,50,40,30]
acc = itertools.accumulate(vals)
print(list(acc))
"""
[10, 20, 30, 40, 50, 50, 50] do maxima v danem poli a pak vraci jen to maximum
max znamena akumulacni funkce
"""
acc = itertools.accumulate(vals, max)
print(list(acc))

# amortize a loan over a set number of payments for a 2000 loan at 4%
"""
[2000, 1980, 1934, 1811, 1778, 1749, 1699, 1657, 1593, 1507, 1467, 1416, 1353]
vytvorena vlastni akumulacni funkce update
mame pocatecni budget 2000 dolaru a pak mame platby ktere se odecitaji 
"""
payments = [100, 125, 200, 105, 100, 120, 110, 130, 150, 100, 110, 120]

update = lambda balance, payment: round(balance * 1.04) - payment
balances = itertools.accumulate(payments, update, initial=2_000)
print(list(balances))
