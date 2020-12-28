#!python3

import re

# Regular expression to detect dates
dateRegex = re.compile(r'''
    (\d{1,2})                   # DD or MM
    ([/.-])                     # seperator 1
    (\d{1,2})                   # DD or MM
    ([/.-])                     # seperator 2
    (\d{2,4})                   # YY or YYYY
    ''', re.VERBOSE)

# User inputs date format they would like to use.
dateFormatDMY = True

if input('''\nWhich date format would you like to use?
        \n1) DD/MM/YYYY
        \n2) MM/DD/YYYY
        \nType '1' or '2': 
        ''') != 1:
    dateFormatDMY = False
else:
    dateFormatDMY = True

# User inputs date
mo = dateRegex.search(input('Input a date: ')).groups()
print("TEST: input match object",mo) #test

# Set DMY variable index numbers
day = mo[0]
month = mo[2]
year = mo[4]

print("TEST: match object, index 0: ",day)
print("TEST: match object, index 0: ",month)
print("TEST: match object, index 0: ",year)


"""
if mo:
    print('Match found.')
    print(mo)
#    print(month, day, year)
else:
    print('No match found.')
"""
