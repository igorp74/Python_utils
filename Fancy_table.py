"""

👔 Igor Perković

⚙ CREATED: 2021-09-18 12:11:52
📆 CHANGED: 2022-04-01 00:13:57

"""

import sys
from tabulate import tabulate

if len(sys.argv):
    # First, join all arguments into one string
    tmp = ' '.join(sys.argv[1:])

    # Then, replace raw string '\n' with some exotic character, which you don't expect to appear in your text
    # all because to distinct the real end-of-line with multiline item for tabulate.
    # (Later, when you split string on end-of-line character, you will revert the change back, so tabulate can make the multiline)
    tmp = tmp.replace(r'\n','§')

    # Now, split the whole string on true end-of-line character (\n)
    str_list = tmp.split('\n')
    # ...and remove empty items from list
    res = list(filter(None, str_list))

    # Reverting back the \n from exotic character (§)
    final = []
    for r in res:
        final.append(r.replace('§','\n'))

    data = []
    for r in final:
        data.append(list(r.split('|')))

    print(tabulate(data,headers='firstrow',colalign=('right',),tablefmt='plain'))
    # print(tabulate(data,headers='firstrow',colalign=('right',),tablefmt='simple'))
    # print(tabulate(data,headers='firstrow',colalign=('right',),tablefmt='fancy_grid'))
    # print(tabulate(data,headers='firstrow',colalign=('right',),tablefmt='psql'))
