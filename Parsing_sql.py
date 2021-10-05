#!/home/igorp/python_venv/data/bin/python
# -*- coding: utf8 -*-

import sys
import sqlparse

if len(sys.argv):
    # Join all arguments into one string
    sql = ' '.join(sys.argv[1:])
    parsed = sqlparse.format(sql, reindent=True, keyword_case='upper')
    print(parsed)