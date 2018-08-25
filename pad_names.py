#!/usr/bin/python3

names = open('names.csv').readlines()

students = open('students.csv', 'a')

for n in names:
    students.write(n[:-1] + ',1,Datalogi\n')
students.close()
