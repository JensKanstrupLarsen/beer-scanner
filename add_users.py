#!/usr/bin/python3
import barcode
import numpy as np
import sqlite3

first_id = 1000

students = np.genfromtxt('students.csv', delimiter=',', dtype=(str))

conn = sqlite3.connect('øllerbøller.db')
c = conn.cursor()

id = first_id
for s in students:
    name, level, faction = s
    query = "(" + str(id) + ",\"" + name + "\",\"" + faction + "\"," + level + ")"
    c.execute("INSERT INTO bøller(id, name, faction, level) VALUES " + query)
    id += 1

conn.commit()
conn.close()
