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

def split_on_delimiter(dc, data_str, mode=0):
    """

    ╒═════════════╤══════════════════════════════════════╤═════════╕
    │   ARGUMENTS │ DESCRIPTION                          │ TYPE    │
    ╞═════════════╪══════════════════════════════════════╪═════════╡
    │          dc │ Delimiter Character(s)               │ string  │
    │             │ Multiple delimiters should           │         │
    │             │ be divided by pipe string '|'        │         │
    ├─────────────┼──────────────────────────────────────┼─────────┤
    │        data │ Selected text                        │ string  │
    ├─────────────┼──────────────────────────────────────┼─────────┤
    │        mode │ 0 = Do not erase non-splittable rows │ int     │
    │             │ 1 = Erase all non-splittable rows    │         │
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

        if mode == 0:
            clean_data.append(row)
        if len(row)>1:
            if mode:
                clean_data.append(row)

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

    # If there is more than one character declared as delimiter,
    # split them on pipe and loop through each of them

    if '|' in res[0]:
        dl = res[0].split('|')
        for e,d in enumerate(dl):
            if e==0:
                txt = split_on_delimiter(d, res[1:])
            else:
                txt = split_on_delimiter(d, txt)

    # Else, proces only single delimiter character
    else:
        txt = split_on_delimiter(res[0], res[1:])

    # Finally print the result
    for t in txt:
        print(t)



