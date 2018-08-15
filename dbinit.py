#!/usr/bin/python3
import sqlite3 as sqlite
import os
import datetime

if os.path.exists ("øllerbøller.db"):
    os.rename ("øllerbøller.db", "backups/øllerbøller" + str(datetime.datetime.now()) + ".db")

f = open("øllerbøller.db", "w").write("")

conn = sqlite.connect("øllerbøller.db")
c = conn.cursor()

c.execute("CREATE TABLE bøller (id int, name text, faction text, level int)")
c.execute("CREATE TABLE øller (id int, product text, price int)")
c.execute("CREATE TABLE øllerbøller (bølle int, ølle int, dato datetimeqty int)")

conn.commit()
conn.close()
