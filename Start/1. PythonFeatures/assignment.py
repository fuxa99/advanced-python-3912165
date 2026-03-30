# Example file for Advanced Python by Joe Marini
# The assignment expression operator := (or the "walrus" operator)

import pprint


# regular assignment statements assign a value
x = 5
print(x)

# the assignment operator is part of an expression 
# x := 10 takto bez zavorek nelze pouzit
(x := 10) # walrus (mroz) operator
print(x)

# The assignment expression is useful for writing concise code
#thestr = input("Value? ")
#while thestr != "exit":
#  print(thestr)
#  thestr = input("Value? ")

#zjendoduseni kodu nahore. lze takto rovnou udelat assignment ve while a nemusime mit multiple input funkci
while (thestr := input("Value? ")) != "exit":
  print(thestr)


# The walrus operator can help reduce redundant function calls
values = [12, 0, 10, 5, 9, 18, 41, 23, 30, 16, 18, 9, 18, 22]
#l = len(values)
#s = sum(values)
#val_data = {
#    "length": l,
#    "total": s,
#    "average": s/l
#}

# prakticka ukazka kde se to da pouzit neni potreba deklraovat dalsi pormene
val_data = {
    "length": (l := len(values)),
    "total": (s := sum(values)),
    "average": s/l
}

pprint.pp(val_data)