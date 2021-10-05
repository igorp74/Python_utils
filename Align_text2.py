#!/home/igorp/python_venv/data/bin/python
# -*- coding: utf8 -*-

"""
🏷️ ALIGN TEXT SIMPLE
👔 Igor Perković

🚀 Created: 2021-10-05 23:05:21
📅 Changed:

💡 Idea is to extend KDE Kate with simple align function.

USAGE:

1. Type delimiter character(s)/word(s)
   in a blank line, before text you want to select and align.
2. Select delimiters along with text
3. Run this script

"""

import sys

def split_on_delimiter(dc, data_str):
    """

    ╒═════════════╤══════════════════════════════════════╤═════════╕
    │   ARGUMENTS │ DESCRIPTION                          │ TYPE    │
    ╞═════════════╪══════════════════════════════════════╪═════════╡
    │          dc │ Delimiter Character(s)               │ string  │
    ├─────────────┼──────────────────────────────────────┼─────────┤
    │        data │ Selected text                        │ string  │
    ╘═════════════╧══════════════════════════════════════╧═════════╛

    """

    data = []
    for r in data_str:
        try:
            data.append(r.split(dc,1))
        except:
            pass

    cw          = 0
    mcw         = 0
    clean_data  = []

    for row in data:
        # If we have split, only then count max length
        # otherwise, just ignore.

        clean_data.append(row)
        if len(row)>1:
            cw = len(row[0].strip())
            if cw > mcw:
                mcw = cw

    col_width = mcw

    result = []
    for row in clean_data:
        if len(row) > 1:
            before = row[0].strip().ljust(col_width)
            after  = row[1].strip()
            final  = f'{before} {dc} {after}'
        else:
            final = row[0]
        result.append(final)
    return result

# Start. Check if we do have any selected text to process ?
if len(sys.argv):

    # Join all others arguments into one string
    tmp = ' '.join(sys.argv[1:])
    # then split them by \n
    res = tmp.split('\n')

    txt = split_on_delimiter(':', res)

    # Finally print the result
    for t in txt:
        print(t)
