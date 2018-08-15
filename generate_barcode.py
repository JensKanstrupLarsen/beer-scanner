#!/usr/bin/python3
import barcode
import numpy as np
import sqlite3

first_id = 1000

students = np.genfromtxt('students.csv', delimiter=',', dtype=(str))

conn = sqlite3.connect('example.db')
