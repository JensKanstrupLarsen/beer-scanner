#!/usr/bin/python3
# coding=utf-8
import numpy as np
import sqlite3
import random

cancel = "0000"
submit = "9999"

greetings = ['Greetings traveler! What is thy name?',
             'What is your name master hobbit?',
             'Pleased to see you! What is your name?']

welcome = []

bartender_requests = ['Scan whatever beverage you desire, and it shall be yours.',
                      'What dost thy thirst for? Scan it and I will retrieve it for you',
                      'What is your desire _ sir?',
                      'How may I aid you master _?',
                      'What supplies do you want for your quest _?']

bartender_replies = ['Your order has been accepted',
                     'Enjoy your purchase',
                     'It has been noted that you have increased the probability of winning the beer cup',
                     'Achievement Unlocked: Buy a(nother) beverage'
                     'MINEFELT: Du skal nu bunde! haha']

conn = sqlite3.connect('øllerbøller.db')
c = conn.cursor()

def grab_a_beer():
    nameID = input("{0}\n".format(greetings[random.randint(0, len(greetings) - 1)]))
    c.execute("SELECT name FROM bøller WHERE id =" + nameID)
    name = c.fetchone()
    if name is None:
        print("I do not recognise your name master hobbit.")
        grab_a_beer()
    # Everything went well!
    name = name[0]

    beer = input("{0}\n".format(bartender_requests[random.randint(0, len(bartender_requests) - 1)]).replace("_", name))

    if beer == nameID:
        print("You have already introduced yourself master hobbit!")
        beer = input("Please try to speak clearly this time!\n")

    # The person scanned is clearly retarded and does not deserve a beer
    if beer == nameID:
        print("DNUR pls")
        grab_a_beer()

    if beer == cancel:
        print("Alright master hobbit. I will keep your beer cold for when you think you're up for the challenge.")
        grab_a_beer()

    try:
        buying = 1
        while buying:
            c.execute("SELECT id, product FROM øller WHERE id =" + beer)
            product = c.fetchone()
            print("You have chosen one " + product[1])
            query = "(\"" + nameID + "\"," + str(product[0]) + ",1)"
            c.execute("INSERT INTO øllerbøller(bølle, ølle, qty) VALUES " + query)
            beer = input("If you want anything else, hobbit, then scan it now. Otherwise tab out by scanning the 'LOGOUT' barcode\n")
            if beer == submit:
                conn.commit()
                print("{0}".format(bartender_replies[random.randint(0, len(bartender_replies) - 1)]))
                buying = 0

            if beer == cancel:
                conn.rollback()
                print("I cannot say I am not disappointed, but if you have coin another time I will have still have wares")
    except:
        print("Something went wrong. Please try again. Nothing has been recorded.")
        conn.rollback()
    grab_a_beer()

grab_a_beer()
