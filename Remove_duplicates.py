#!/home/igorp/python_venv/data/bin/python
# -*- coding: utf8 -*-

import sys

if len(sys.argv):
    # Join all arguments into one string
    tmp = ' '.join(sys.argv[1:])
    # then split them by \n
    res = tmp.split('\n')

    # Accumulate the result in this list
    acc = []
    for i in res:
        # if list item is not already in accumulated list
        if i not in acc:
            acc.append(i)
    # If last element of list is empty string, remove it from a list
    if acc[-1] == '':
        acc.pop()
    # Finaly join back to a string delimited with \n
    final = '\n'.join(acc)
    # Print the final result
    print(final)
