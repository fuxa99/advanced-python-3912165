# Example file for Advanced Python by Joe Marini
# Sequence comparisons

import itertools


# define some lists
seq1 = [1, 2, 3, 6, 10, 15, 34, 56] #list
seq2 = [1, 2, 5, 7, 9, 18, 22, 38, 91]

# define a tuple
seq3 = (1, 2, 3, 6, 10, 15, 34, 56) #tuple

# compare the sequences
print(seq1 == seq2)
print(seq1 > seq2) # prtoze 3 hodnota v seq1 je evtsi nez v seq2 
print(seq1 < seq2) # a tu je to obrazene zase jelikoz 5 > 3

# sequences that have equal values but different number of items:
seq4 = [10, 20, 30]
seq5 = [10, 20, 30, 40, 50]

print(seq5 > seq4) # True jelikoz to ma vice hodnot 

# Sequences must be of the same type to be compared
print(seq1 == seq3) #je to false jelikoz jedne je list a druhy tuple

print(tuple(seq1) == seq3) # ted to bude True

# use the all() function to compare two arbitrary sequences
result = all(x == y for x,y in itertools.zip_longest(seq1,seq3)) # vice memeory efficient
print(result) # True