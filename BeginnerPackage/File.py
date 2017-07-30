import random
import os
import sys

#File operations
test_file = open("test.txt", "wb")
print(test_file.name, test_file.mode)
test_file.write(bytes ("This is a test file\n"))
test_file.close()

test_file = open("test.txt", "r+")
text = test_file.read()
print(text)
test_file.close()



