#!/usr/bin/python3
import barcode
import numpy as np
import sqlite3

conn = sqlite3.connect('øllerbøller.db')
c = conn.cursor()

c.execute("""
            SELECT bøller.name, øller.product, COUNT(øller.id) FROM øllerbøller
                INNER JOIN øller ON øllerbøller.ølle = øller.id
                INNER JOIN bøller ON øllerbøller.bølle = bøller.id
                GROUP BY bøller.id, øller.product
            """)
names = c.fetchall()
for name in names:
    print(name)

conn.commit()
conn.close()
