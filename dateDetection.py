#!python3

import re

dateRegex = re.compile(r'''
    (\d{1,2})                   # DD or MM
    ([/.-])                     # seperator 1
    (\d{1,2})                   # DD or MM
    ([/.-])                     # seperator 2
    (\d{2,4})                   # YY or YYYY
    ''', re.VERBOSE)

# User inputs date format
dateFormatDMY = True

if input('''\nWhich date format would you like to use?
        \n1) DD/MM/YYYY
        \n2) MM/DD/YYYY
        \nType '1' or '2': 
        ''') != 1:
    dateFormatDMY = False
else:
    dateFormatDMY = True

dates = []

mo = dateRegex.findall(input('Input a date: '))
if mo:
    #dates.append()
    print('Match found.')
    #print(mo.groups([0]))
else:
    print('No match found.')
