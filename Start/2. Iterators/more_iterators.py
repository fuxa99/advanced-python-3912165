# Example file for Advanced Python by Joe Marini
import itertools

# define a list of days in English and French
"""
1 Sun
2 Mon
3 Tue
4 Wed
5 Thu
6 Fri
7 Sat
"""

days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

for d in range(len(days)):
  print(d+1, days[d])

# the enumerate function
# enumare vezme kolekci spolecne se startovaci hodnotou a vrati tuple kde je index value a item
for i, d in enumerate(days, start=1):
  print(i, d)

# use zip to combine sequences
"""
('Sun', 'Dim')
('Mon', 'Lun')
('Tue', 'Mar')
('Wed', 'Mer')
('Thu', 'Jeu')
('Fri', 'Ven')
('Sat', 'Sam')
"""
for d in zip(days, daysFr):
  print(d)

# use enumerate and zip together
"""
1 Sun = Dim in French
2 Mon = Lun in French
3 Tue = Mar in French
4 Wed = Mer in French
5 Thu = Jeu in French
6 Fri = Ven in French
7 Sat = Sam in French - pokud by v jednom poli chybel item napriklad Sam tak for skonci u Friday,
bere nejrkatsi sekvenci
"""
for i, d in enumerate(zip(days, daysFr), start=1):
  print(i, d[0], "=", d[1], "in French")

# use zip_longest
seq1 = ["A","B","C","D","E","F"]
seq2 = [1, 2, 3, 4]
seq3 = "xyz"

"""
Result: 
('A', 1, 'x')
('B', 2, 'y')
('C', 3, 'z')
('D', 4, '-')
('E', '-', '-')
('F', '-', '-')
"""
# zip por nejdelsi sequency
result = itertools.zip_longest(seq1, seq2, seq3, fillvalue="-")
print("Result: ")
for item in result:
  print(item)