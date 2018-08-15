#!/usr/bin/python3
import barcode
import numpy as np
import sqlite3

conn = sqlite3.connect('øllerbøller.db')
c = conn.cursor()

c.execute("SELECT * FROM bøller")
print(c.fetchall())
c.execute("SELECT * FROM øller")
print(c.fetchall())

conn.commit()
conn.close()
