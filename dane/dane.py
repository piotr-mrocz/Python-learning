#! /usr/bin/env python

import sqlite3

# utworzenie poĹ‚Ä…czenia z bazÄ… przechowywanÄ… na dysku
# lub w pamiÄ™ci (':memory:')
con = sqlite3.connect('ksiazki.sql')

## dostÄ™p do kolumn przez indeksy i przez nazwy
#con.row_factory = sqlite3.Row

# utworzenie obiektu kursora
cur = con.cursor()

cur.execute("SELECT * FROM ksiazki")
records = cur.fetchall()

for record in records:
    print (record)