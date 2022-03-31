# -*- coding: utf8 -*-

"""
🏷️ ALIGN TEXT SIMPLE
👔 Igor Perković

🚀 Created: 2021-10-05 23:05:21
📅 Changed: 2022-01-23 19:20:14

💡 Idea is to extend KDE Kate with simple align function.

USAGE:

1. Type delimiter character(s)/word(s)
   in a blank line, before text you want to select and align.
2. Select delimiters along with text
3. Run this script

"""

import sys
import numpy as np
import pandas as pd

def align_delimited_text(txt, mode=0):
    if len(txt):
        res = txt.split('\n')
        delimiter = res[0]

        acc = []
        # NOTE 💡 The Idea here is to mark these rows who contains delimiter in a new column at first position [0]
        # and then calculate max columns length on these rows where delimiter exists.
        # ----------------------------------------------------------------------------------------------------------
        for e,d in enumerate(res[1:]):
            if delimiter in d:
                dn = '1' + delimiter + d
            else:
                dn = '0' + delimiter + d
            tmp = dn.split(delimiter)
            acc.append(tmp)

        df = pd.DataFrame(acc)

        # Filter splitted - to see in which row exists delimiter
        dff = df[df[0]=='1']

        # After we choose the rows and subset of data for column width measurements,
        # we may drop this column with indicator
        #----------------------------------------------------------------------------
        dff = dff.drop(dff.columns[[0]], axis=1)
        df  = df.drop(df.columns[[0]], axis=1)

        dfl = df.columns.tolist()

        col_widths = np.vectorize(len)
        cw = col_widths(dff.values.astype(str)).max(axis=0)

        cwl = []
        for i in cw:
            cwl.append(i)

        for x,y in zip(dfl, cwl):
            df[x]=df[x].str.ljust(y)

        df = df.replace(np.nan, '')
        rowres = []
        for v in df.values.tolist():
            rowstr = ''
            for e,i in enumerate(v):
                if e:
                    if len(i.strip()):
                        if mode:
                            rowstr = rowstr + f'{delimiter}' + i
                        else:
                            rowstr = rowstr + ' ' + i
                else:
                    if len(i.strip()):
                        rowstr = rowstr + i
            rowres.append(rowstr)

        for t in rowres:
            print(t)

# Start. Check if we do have any selected text to process ?
if len(sys.argv):
    # Join all arguments into one string
    tmp = ' '.join(sys.argv[1:])
    try:
        align_delimited_text(tmp, mode=1)
    except:
        print(tmp)
        print('Please check 1st line delimiter...')
