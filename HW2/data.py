import sqlite3
from pprint import pprint
conn = sqlite3.connect('bicycle.db')
c=conn.cursor()
c.execute('SELECT HiTemp, LoTemp, Precip, Manhattan FROM bicycle')
data=c.fetchall()
pprint (data)
conn.close() 