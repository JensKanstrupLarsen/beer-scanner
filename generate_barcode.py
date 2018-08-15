#!/usr/bin/python3
import barcode
import numpy as np
import sqlite3

conn = sqlite3.connect('øllerbøller.db')
c = conn.cursor()

c.execute("SELECT * FROM bøller")
bøller = c.fetchall()

code128 = barcode.get_barcode_class('code128')

conn.close()
