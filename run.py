#!/usr/bin/python3
# coding=utf-8
import numpy as np
import sqlite3

cancel = "0000"
submit = "9999"

conn = sqlite3.connect('øllerbøller.db')
c = conn.cursor()

while 1:
    nameID = input("Greetings!\n")
    c.execute("SELECT name FROM bøller WHERE id =" + nameID)
    name = c.fetchone()[0]
    print("Velkommen " + name)
    line = input("Scan din drikkevare\n")
    while 1:
        if line == nameID:
            print(name + " er allerde logget ind.")
            line = input("Scan drikkevarer eller LOG UD. Scan ANNULER hvis du fortryder dit køb\n")
        else:
            if line == cancel:
                print("Du annulerede dit køb. Tag IKKE drikkevarer")
                conn.rollback()
                break
            if line == submit:
                print("Dit køb blev gennemført. Skål!")
                conn.commit()
                break
            c.execute("SELECT id, product FROM øller WHERE id =" + line)
            product = c.fetchone()
            print("Du har valgt 1 " + product[1])
            query = "(\"" + nameID + "\"," + str(product[0]) + ",1)"
            c.execute("INSERT INTO øllerbøller(bølle, ølle, qty) VALUES " + query)
            line = input("Scan flere drikkevarer, eller scan LOG UD for at afslutte købet\n")
