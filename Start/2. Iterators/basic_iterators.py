# Example file for Advanced Python by Joe Marini
# Working with basic iterators

# define a list of days in English and French
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

# use regular interation over the days
"""
Sun Mon Tue Wed Thu Fri Sat
"""
for d in days:
    print(d)

# use iter() to create an iterator over a collection, vytvori iterovatelny objekt
# the next() function retrieves the next value from an iterator
i = iter(days)
""" Sun Mon Tue """
print(next(i), next(i), next(i))

# iterate using a function and a sentinel
with open("Start/2. Iterators/testfile.txt", "r") as fp:
    # pokud return hodnota z fp.readline je '' tak iterator se zastavi
    for line in iter(fp.readline, ''):
        print(line)