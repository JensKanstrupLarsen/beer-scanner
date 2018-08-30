#!/usr/bin/python3
import barcode
import numpy as np
import sqlite3


# To be covered in with the other beverage sale
# mad_purchase_price = 600 
extra_expenses = 2000 # TBA not real price


# Total cost of each beverage
beer = 5.6 # 130/30 - 4,3 kr 
soda = 4.1 # 80/30 - 2,6
cocio = 11.3 # 136/16 - 8,5
cider = 15.3 # 300/24 - 12,5
mad = 0

# Hvor mange streget
beer_noted = 1180
soda_noted = 172
cocio_noted = 161
cider_noted = 255
mad_noted = 0

# Hvor mange drukket
beer_count = 1290
soda_count = 168
cocio_count = 193
cider_count = 288
mad_count = 0

beer_noted_price = (beer_noted + 214) * beer
beer_count_price = beer_count * 4.3 
beer_price_diff  = beer_noted_price - beer_count_price

soda_noted_price = (soda_noted + 16) * soda
soda_count_price = soda_count * 2.6
soda_price_diff  = soda_noted_price - soda_count_price

cocio_noted_price = cocio_noted * cocio
cocio_count_price = cocio_count * 8.5
cocio_price_diff  = cocio_noted_price - cocio_count_price

cider_noted_price = cider_noted * cider
cider_count_price = cider_count * 12.5
cider_price_diff  = cider_noted_price - cider_count_price

mad_noted_price = mad_noted * mad
mad_count_price = 600
mad_price_diff  = mad_noted_price - mad_count_price

total_diff = (beer_price_diff + soda_price_diff + cocio_price_diff + cider_price_diff - extra_expenses)

print("Beer profits: ", beer_price_diff - 214 * beer)
print("Soda profits: ", soda_price_diff - 16  * soda)
print("Cocio profits:", cocio_price_diff)
print("Cider profits:", cider_price_diff)
print("Mad profits:",   mad_price_diff)
print("Total Difference:", total_diff)


beer_diff = beer_noted - beer_count
soda_diff = soda_noted - soda_count
cocio_diff = cocio_noted - cocio_count
cider_diff = cider_noted - cider_count
mad_diff = mad_noted - mad_count


print("\nStreg vs talt:")
print("beer: " + str(beer_diff) + "\nsoda: " + str(soda_diff) + "\ncocio: " + str(cocio_diff) + "\ncider: " + str(cider_diff) + "\nmad: " + str(mad_diff))

conn = sqlite3.connect('øllerbøller.db')
c = conn.cursor()

c.execute("""
            SELECT bøller.name, øller.product, COUNT(øller.id) FROM øllerbøller
                INNER JOIN øller ON øllerbøller.ølle = øller.id
                INNER JOIN bøller ON øllerbøller.bølle = bøller.id
                GROUP BY bøller.id, øller.product
                
            """)

names = c.fetchall()

users = {n[0]: {} for n in names}

to_pay = {n[0]: 0 for n in names}

for name in names:
    users[name[0]][name[1]] = name[2]
    if name[1] == 'øl':
        to_pay[name[0]] += name[2]*beer
    elif name[1] == 'sodavand':
        to_pay[name[0]] += name[2]*soda
    elif name[1] == 'cocio':
        to_pay[name[0]] += name[2]*cocio
    elif name[1] == 'cider':
        to_pay[name[0]] += name[2]*cider



print(users)
print(to_pay)


conn.commit()
conn.close()