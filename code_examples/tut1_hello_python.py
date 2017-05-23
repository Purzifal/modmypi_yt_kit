#!/usr/bin/python3.4

'''
Basic introdution to python on raspberry pi
'''

print('=== The Print Statement ===')
# Print Statement - This will print something to the console
# and is handy for debugging situations
print('This prints something to the console')

print('\n=== Using Variables ===')
# Variables - Stores data that can be used how you wish
# Variables can be used to add data to and call data from them
VAR_1 = 'Hello'
VAR_2 = 'Python'

print(VAR_1)
print(VAR_2)

print('\n=== Using Variables & Math Operations ===')
# You can use some math operatons with strings
# NOTE: this can end up looking messy with complex strings
print(VAR_1 + ' ' + VAR_2)

print('\n=== Using String Formatting ===')
# Using the string formatting does the same as above
# but makes strings easier to read with complex strings
print('{} {} !!'.format(VAR_1, VAR_2))
print('the 1st variable is {first} and 2nd is {second} !!'.format(second=VAR_2, first=VAR_1))
