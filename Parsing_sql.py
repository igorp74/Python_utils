# -*- coding: utf8 -*-

# 📦 PACKAGE:
# pip install sqlparse

import sys
if len(sys.argv):
    # Join all arguments into one string
    sql = ' '.join(sys.argv[1:])

    import sqlparse
    parsed = sqlparse.format(sql, indent_width=4, reindent_aligned=True, use_space_around_operators=True, comma_first=True, keyword_case='upper')
    print(parsed)
