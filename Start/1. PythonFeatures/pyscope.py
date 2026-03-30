# Example file for Advanced Python by Joe Marini
# Understanding Python scope
"""
pred pridanim - global x
$ /usr/local/bin/python "/workspaces/advanced-python-3912165/Start/1. PythonFeatures/pyscope.py"
10 - z funkce ktera nemeni globalni hodnotu
1 - globalni x 
6 - globalni x + 5 
10 - nezmenene x ve funkci

po tom co udelame global x tak se stane x globalni a uvnitr funkce se uz i meni hodnota x
$ /usr/local/bin/python "/workspaces/advanced-python-3912165/Start/1. PythonFeatures/pyscope.py"
10
10
15
10
"""

## declare a variable within the global scope
#x = 1
#
## define a local function with a variable "x"
#def myFunc():
#  global x
#  x = 10
#  print(x)
## Run the test function and observe the two results
#myFunc()
#print(x)
#
#x = x + 5
#print(x)
#myFunc()
#


"""
$ /usr/local/bin/python "/workspaces/advanced-python-3912165/Start/1. PythonFeatures/pyscope.py"
20
30
30
45
"""
# Nested functions create inner scopes. These are called closures:
def multiplayer_maker(factor):
  def multiply(num):
    return num * factor
  return multiply

doubler = multiplayer_maker(2)
tripler = multiplayer_maker(3)

print(doubler(10))
print(doubler(15))
print(tripler(10))
print(tripler(15))