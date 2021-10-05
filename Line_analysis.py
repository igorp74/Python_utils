#!/home/igorp/python_venv/data/bin/python
# -*- coding: utf8 -*-

"""
TEXT LINE ANALYSIS

🏷️ Kate External Tool
👔 Igor Perković

🚀 Created: 2021-08-27 20:41:18
📅 Changed:


💡 IDEA: Analyse text lines and shows 3 categoriers:
         1. Unique lines from all text
         2. Unique lines just from duplicates
         3. Pure unique lines

"""

import sys

if len(sys.argv):
    # Join all arguments into one string
    tmp = ' '.join(sys.argv[1:])
    # then split them by \n
    res = tmp.split('\n')

    # Creating an empty dictionary
    freq = {}
    for i in res:
        if (i in freq):
            freq[i] += 1
        else:
            freq[i] = 1

    acc = []
    unique = []
    unique_of_duplicates = []

    for key, value in freq.items():
        acc.append(key)
        if value == 1:
            unique.append(key)
        else:
            unique_of_duplicates.append(key)


    # Finaly join back to a string delimited with \n
    f_all = '\n'.join(acc)
    f_uni = '\n'.join(unique)
    f_uod = '\n'.join(unique_of_duplicates)

    # Print the final result
    print('⚙️ All unique lines')
    print('------------------')
    print(f_all)
    print('\n⛓️ Unique just from duplicate lines')
    print('------------------------------------')
    print(f_uod)
    print('\n📎 Pure Unique Lines')
    print('---------------------')
    print(f_uni)

