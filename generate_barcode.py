#!/usr/bin/python3
import barcode
import numpy as np
import sqlite3

conn = sqlite3.connect('øllerbøller.db')
c = conn.cursor()

c.execute("SELECT * FROM bøller")
bøller = c.fetchall()

CODE128 = barcode.get_barcode_class('code128')
for b in bøller:
    code128 = CODE128(str(b[0]))
    code128.save("barcodes/" + "_".join(b[1].split(" ")))
conn.close()
