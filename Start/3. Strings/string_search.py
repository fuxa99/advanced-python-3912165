# Example file for Advanced Python by Joe Marini


sample_text = "The quick brown fox jumps over the lazy dog."
lower_sample_text = sample_text.lower()
# Using find() to find the first occurrence of a substring
"""
First occurrence od 'the' 31 je to totiz zavisle na velioksti pismen 
kdyz pridame prevedeni la lower tak to najde prvni
First occurrence od 'the' 0
"""
print("First occurrence od 'the'", lower_sample_text.find("the"))

# Example with optional start and end parameters
# kde ma hledat od jakeho do jakeho 
print("First occurrence od 'fox'", sample_text.find("fox",5,36))

# Using index() to find the first occurrence of a substring (raises ValueError if not found)
# Not found
try:
  print("First occurrence od 'fox'", sample_text.index("fax"))
except ValueError:
  print("Not found")
# The 'in' operator can be used for Boolean testing:
# Is 'fox' present: True
print("Is 'fox' present:", "fox" in sample_text )

# Using rfind() to find the last occurrence of a substring
"""
Last occurrence of 'the': 31
"""
print("Last occurrence of 'the':", lower_sample_text.rfind('the'))

# Using rindex() to find the last occurrence of a substring (raises ValueError if not found)
try:
  print("Last occurrence of 'the':", lower_sample_text.rindex('thhh'))
except ValueError:
  print("Not found")

# The replace() function will find content in the string and replace it
"""
The quick brown fox jumps over the tired dog.
"""
result = sample_text.replace("lazy", "tired")
print(result)
