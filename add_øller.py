#!/usr/bin/python3
import barcode
import numpy as np
import sqlite3

øller = [["øl", 6], ["cider", 20]]

conn = sqlite3.connect('øllerbøller.db')
c = conn.cursor()

for ø in øller:
    query = "(\"" + ø[0] + "\"," + str(ø[1]) + ")"
    c.execute("INSERT INTO øller(product, price) VALUES " + query)

conn.commit()
conn.close()
