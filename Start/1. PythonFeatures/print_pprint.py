# Example file for Advanced Python by Joe Marini
# using the print() and pprint() functions

import pprint
from dataclasses import dataclass

# The print() function has useful parameters to help you format
# output for increased readability
# basic print() function
values=["one", "two", "three", "four", "five"]
print(*values)

# use the 'sep' argument to control the separator between values:
""" one -- two -- three -- four -- five """
print(*values, sep = " -- ")

# use the 'end' argument to control the line ending characters
# let's auto-print the current line number along with each item
"""
one [line]: 1 
two [line]: 2 
three [line]: 3 
four [line]: 4 
five [line]: 5 
"""
for i in range(0, len(values)):
    print(values[i], end=f" [line]: {str(i+1)} \n")

# you can even redirect print() output to a file:
newfile = open("/workspaces/advanced-python-3912165/Start/1. PythonFeatures/output.txt", "w")
print(*values, sep=" -- ", file=newfile, flush=True)
# flush rekne aby po kazdem print zapsal do souboru a necekal az se mu naplni vsim

# pprint() can be used to print more complex data 
# in a format that is more readable
worldcupdata = [
    { "game": "Final", "Attendance" : 88966, "Argentina" : "3 (4)", "France" : "3 (2)" },
    { "game": "3rd Place", "Attendance" : 44137, "Croatia" : 2, "Morocco" : 1},
    { "game": "Semifinal", "Attendance" : 68294, "France" : 2, "Morocco" : 0},
    { "game": "Semifinal", "Attendance" : 88966, "Argentina" : 3, "Croatia" : 0}
]
"""
[{'game': 'Final',
  'Attendance': 88966,
  'Argentina': '3 (4)',
  'France': '3 (2)'},
 {'game': '3rd Place', 'Attendance': 44137, 'Croatia': 2, 'Morocco': 1},
 {'game': 'Semifinal', 'Attendance': 68294, 'France': 2, 'Morocco': 0},
 {'game': 'Semifinal', 'Attendance': 88966, 'Argentina': 3, 'Croatia': 0}]
"""
pprint.pp(worldcupdata)

"""
[  {  'game': 'Final',
      'Attendance': 88_966,
      'Argentina': '3 (4)',
      'France': '3 (2)'},
   {  'game': '3rd Place',
      'Attendance': 44_137,
      'Croatia': 2,
      'Morocco': 1},
   {  'game': 'Semifinal',
      'Attendance': 68_294,
      'France': 2,
      'Morocco': 0},
   {  'game': 'Semifinal',
      'Attendance': 88_966,
      'Argentina': 3,
      'Croatia': 0}]
"""
pprint.pp(worldcupdata, indent=3, width=40, underscore_numbers=True)

# pprint also works on newer complex structures, like dataclasses!
@dataclass
class wcdata:
    game: str
    attendance: int
    team1: str
    team2: str
    score: str

worldcupdata2 = [
    wcdata("Final", 88966, "Argentina" , "France" , "3 (4) -- 3 (2)" ),
    wcdata("3rd Place", 44137, "Croatia" , "Morocco" , "2 -- 1" ),
    wcdata("Semifinal", 68294, "France" , "Morocco" , "2 -- 0" ),
    wcdata("Semifinal", 88966, "Argentina" , "Croatia" , "3 -- 0" ),
]

"""
[wcdata(game='Final',
        attendance=88966,
        team1='Argentina',
        team2='France',
        score='3 (4) -- 3 (2)'),
 wcdata(game='3rd Place',
        attendance=44137,
        team1='Croatia',
        team2='Morocco',
        score='2 -- 1'),
 wcdata(game='Semifinal',
        attendance=68294,
        team1='France',
        team2='Morocco',
        score='2 -- 0'),
 wcdata(game='Semifinal',
        attendance=88966,
        team1='Argentina',
        team2='Croatia',
        score='3 -- 0')]
"""
pprint.pp(worldcupdata2)