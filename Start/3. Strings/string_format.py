# Example file for Advanced Python by Joe Marini
# Formatting output strings

# https://docs.python.org/3/library/string.html

# Basic formatting - center(), ljust(), rjust()
"""
-----------------center-----------------
ljust-----------------------------------
-----------------------------------rjust
"""
width = 40
print("center".center(width, "-"))
print("ljust".ljust(width, "-"))
print("rjust".rjust(width, "-"))

# Formatting strings with format specification codes
# Format spec is: [[fill]align][sign]["z"]["#"]["0"][width][grouping_option]["."precision][type]
val1 = 1234.5678
val2 = 10987.65
val3 = 12.99
val4 = -280.7

print(f"{val1}")
print(f"{val2}")
print(f"{val3}")
print(f"{val4}")

# Specify a precision and type
"""
1234.57
10987.65
12.99
-280.70
"""
print(f"{val1:.2f}") # zaokrouhleni na dve desetina mista se specifikaci float number
print(f"{val2:.2e}") # 1.10e+04
print(f"{val3:.2f}")
print(f"{val4:.2f}")


# Use alignment and width and leading zeros
# < is left align, > is right align, ^ is centered
"""
   1234.57
 10987.65 
12.99     
   -280.70
"""
print(f"{val1:>10.2f}")
print(f"{val2:^10.2f}")
print(f"{val3:<10.2f}")
print(f"{val4:>10.2f}")

# Use a grouping option and +/- signs
"""
 +1,234.57 - carka zpusobi ze tisice rozdeli carkou 
  10987.65
    +12.99
   -280.70
"""
print(f"{val1:+10,.2f}")
print(f"{val2:-10.2f}")
print(f"{val3:+10.2f}")
print(f"{val4:-10.2f}")

# Insert a fill character
"""
_+1,234.57
__10987.65
____+12.99
___-280.70
"""
print(f"{val1:_>+10,.2f}")
print(f"{val2:_>-10.2f}")
print(f"{val3:_>+10.2f}")
print(f"{val4:_>-10.2f}")

# Create format specifiers dynamically
"""
    123.46
"""
width = 10
precision = 2
format_spec = f"{123.456:{width}.{precision}f}"
print(format_spec)

"""
  10987.65
"""
format_spec = "{val:{width}.{precision}f}".format(val=val2, width=10, precision=2)
print(format_spec)