#!/usr/bin/python3

import urllib.request
import sqlite3
import csv,os

db_filename = 'numbersdb'
db_is_new = not os.path.exists(db_filename)

# Downloads the new number list
def get_numbers():
    historical_numbers = urllib.request.urlretrieve("http://txlottery.org/export/sites/lottery/Games/Mega_Millions/Winning_Numbers/megamillions.csv", "lottery_numbers.csv")

get_numbers()
print("Success")

# Expand this section...
#if db_is_new:
#    print("Need to create schema")
#else:
#    print("Database exists, assuming schema does too.")

# Connect to the SQLite3 database
conn = sqlite3.connect('numbersdb')
c = conn.cursor()

# If the table exists delete it
c.execute("DROP TABLE IF EXISTS numbers")
# Create the table
c.execute("CREATE TABLE numbers (name varchar(13), month int, day int, year int, num1 int, num2 int, num3 int, num4 int, num5 int, num6 int, num7 int)")
conn.commit()

# Load the csv file
csvfile = open('lottery_numbers.csv', 'rt')
creader = csv.reader(csvfile)

# Inserting records in to the database
for t in creader:
    c.execute("INSERT INTO numbers VALUES(?,?,?,?,?,?,?,?,?,?,?)", t )

# Close the csv file
csvfile.close()
# Saving the changes
conn.commit()
# Closing the connection
conn.close()
print("The database has been updated")
