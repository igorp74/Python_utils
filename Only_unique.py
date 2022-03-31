# -*- coding: utf8 -*-

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
    for key, value in freq.items():
        if value == 1:
            acc.append(key)

    if acc[-1] == '':
        acc.pop()
    # Finaly join back to a string delimited with \n
    final = '\n'.join(acc)
    # Print the final result
    print(final)
