# Example file for Advanced Python by Joe Marini
# Manipulating string content


test_str = "The quick, brown fox jumps over the lazy dog."

# upper, lower, title
"""
THE QUICK, BROWN FOX JUMPS OVER THE LAZY DOG.
the quick, brown fox jumps over the lazy dog.
The Quick, Brown Fox Jumps Over The Lazy Dog.

kazda z techot operaci vytvori dalsi string
Python stringy jsou immutable kdyz se vytvori takze je potreba dat bacha kdyz
pracuje s velkymi soubory
"""
print(test_str.upper())
print(test_str.lower())
print(test_str.title())

# strip, lstrip, rstrip
"""
'This string has whitespace'
'   This string has whitespace'
'This string has whitespace '
"""
test_str2 = "   This string has whitespace   "
print(test_str2.strip())
print(test_str2.rstrip())
print(test_str2.lstrip())
# split creates a sequence from a single string
"""
['The', 'quick,', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
"""
words = test_str.split()
print(words)

"""
['The quick', ' brown fox jumps over the lazy dog.']
"""
words = test_str.split(",")
print(words)

# join concatenates an iterable into a single string
words = ["Hello", "world", "from", "Python"]
"""Hello world from Python"""
separator = " "
sentence = separator.join(words)
print(sentence)

"""Hello--world--from--Python"""
separator = "--"
sentence = separator.join(words)
print(sentence)