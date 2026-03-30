# Example file for Advanced Python by Joe Marini
# Itertools: chain, chain.from_iterable

import itertools


# chain() creates a single iterable from multiple
"""
['A', 'B', 'C', 'D', '1', '2', '3', '4', '5', '6']
"""
x = itertools.chain("ABCD", "123456")
print(list(x))

# make a prepend function
"""
['A', 'B', 'C', 'D', 'E']
"""
def prepend(val, iterable):
  return itertools.chain([val], iterable)

print(list(prepend("A","BCDE")))

# chain.from_iterable is an alternate usage of chain
"""
['A', 'B', 'C', 'D', 'E', 'F', 'G', 1, 2, 3, 4, 5, '$', '%', '@', '&']
"""
s1 = "ABCDEFG"
s2 = [1,2,3,4,5]
s3 = ['$','%','@','&']

result  = itertools.chain.from_iterable([s1,s2,s3])
print(list(result))