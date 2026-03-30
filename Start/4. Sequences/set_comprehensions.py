# Example file for Advanced Python by Joe Marini
# Demonstrate how to use set comprehensions

# define a list of temperature data points
ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]

# build a set of unique Fahrenheit temperatures
ftemps1 = [(t * 9/5) + 32 for t in ctemps]
ftemps2 = {(t * 9/5) + 32 for t in ctemps} #syntax for set comphre {}
print(ftemps1) # [41.0, 50.0, 53.6, 57.2, 50.0, 73.4, 105.8, 86.0, 53.6, 75.2, 53.6, 64.4, 84.2]
print(ftemps2) # {64.4, 73.4, 41.0, 105.8, 75.2, 50.0, 84.2, 53.6, 86.0, 57.2} only unique values

# build a set from an input source
"""
{'R', 'D', 'L', 'T', 'J', 'N', 'H', 'C', 'B', 'U', 'Q', 'F', 'Y', 'A', 'G', 'K', 'W', 'X', 'O', 'Z', 'V', 'M', 'P', 'I', 'E'}
"""
sTemp = "The quick brown fox jumped over the lazy dog"
chars = {c.upper() for c in sTemp if not c.isspace()} # unique characters in the list 
print(chars)