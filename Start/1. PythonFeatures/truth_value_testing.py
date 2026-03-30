"""
$ /usr/local/bin/python "/workspaces/advanced-python-3912165/Start/1. PythonFeatures/truth_value_testing.py"
False False
True True
"""

x = []
y = {}

print(bool(x), bool(y))

x = [1]
y = {"key": 5}

print(bool(x), bool(y))