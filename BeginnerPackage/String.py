import random
import os
import sys

#String operations
name = "Praful"
print (name)
single_line_quote = "This is basic Python Course."
multi_line_quote = '''And it's very
interesting indeed'''
print (single_line_quote + multi_line_quote)

new_string = "My name is Anthony Gonsalvis"

print (new_string[2:7])
print (new_string[:-7])
print (new_string[-7:], "is it?")
print("%c is %s letter of %s and %d is first %s number and is greater than %.6f" %
      ( "A", "first", 'alphabets', 1, 'natural', 0.25))
print(new_string.capitalize())
print(new_string.find('Gonsalvis'))
print(new_string.replace('Anthony', 'Johnny'))
print(new_string.isalpha())
print(new_string.isalnum())
print(len(new_string))
print(new_string.strip())
quote_list = new_string.split("y")
print(quote_list)

