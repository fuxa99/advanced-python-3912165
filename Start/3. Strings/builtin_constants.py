# Example file for Advanced Python by Joe Marini
# Using the built-in string constants

import string
import secrets

# built-in constants for a variety of needs
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase) # abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase) # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits) # 0123456789
print(string.hexdigits) # 0123456789abcdefABCDEF
print(string.punctuation) # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


# Define a test string
testStr = "The quick brown fox jumps OVER the lazy dog."

# use an iterator to see if a string contains any punctuation 
if any(c in string.punctuation for c in testStr):
  print("The string contains punctuation")
else:
  print("No punctuation found")

# generate a secure random password
alphabet = string.ascii_letters + string.digits + string.punctuation

password = ''.join(secrets.choice(alphabet) for i in range(10))
print(password) # fvsA}<2,t: example of password

# Check the strength of a password
"""
MyTestPa$$123! is strong password
password is weak password
pa$$w0rd! is weak password
"""
def check_password_strength(testPass):
  if (len(testPass) >= 10 and
      any(char in string.punctuation for char in testPass) and
      any(char in string.digits for char in testPass) and
      any(char in string.ascii_letters for char in testPass)):
    return f"{testPass} is strong password"
  return f"{testPass} is weak password"

print(check_password_strength("MyTestPa$$123!"))
print(check_password_strength("password"))
print(check_password_strength("pa$$w0rd!"))
