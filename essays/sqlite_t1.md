---
layout: essay
type: essay
title: Stock Analysis
date: 2017-09-05
labels:
  - Data Analysis
  - Programming
---

```python
#matplotlib style 
import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
plt.style.use('fivethirtyeight')
conn=sqlite3.connect('tutorial.db')
c=conn.cursor()
```


```python
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')
def data_entry():
    c.execute('INSERT INTO stuffToPlot VALUES(145123542, "2016-01-01", "Python", 5)')
def dynamic_data_entry():
    unix=time.time();# get time stamp
    date=str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword='Python'
    value=random.randrange(0,10)
    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES(?,?,?,?)", (unix, date, keyword, value))
    # you can also only select only a few columns
def read_from_db():
    c.execute('SELECT * FROM stuffToPlot')
    data=c.fetchall()
    #print(data)
    for row in data:
        #print(row[0])
        print(row)
def graph_data():
    #c.execute('DELETE FROM stuffToPlot')
    c.execute('SELECT unix, value FROM stuffToPlot')
    dates=[]
    values=[]
    for row in c.fetchall():# you are only allowed to fetchall once 
        #print(row[0])
        #print(datetime.datetime.fromtimestamp(row[0]))#get date-time from unix timestamp
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])
    plt.plot(dates, values, '-')
    plt.show()
def del_and_update():
    c.execute('SELECT * FROM stuffToPlot')
    [print(row)for row in c.fetchall()]
    print()
    c.execute('UPDATE stuffToPlot set value=6 WHERE value=99')
    
    c.execute('SELECT * FROM stuffToPlot')
    [print(row)for row in c.fetchall()]
```


```python
#create_table()
#data_entry()
#for i in range(10):
#    dynamic_data_entry()
#    time.sleep(1)
#read_from_db()
#graph_data()
del_and_update()
conn.commit()
c.close()
conn.close()
```

    (1504645987.6520224, '2017-09-05 11:13:07', 'Python', 0.0)
    (1504645988.661296, '2017-09-05 11:13:08', 'Python', 3.0)
    (1504645989.6734655, '2017-09-05 11:13:09', 'Python', 99.0)
    (1504645990.6875265, '2017-09-05 11:13:10', 'Python', 3.0)
    (1504645991.6941302, '2017-09-05 11:13:11', 'Python', 4.0)
    (1504645992.7065065, '2017-09-05 11:13:12', 'Python', 9.0)
    (1504645993.7204556, '2017-09-05 11:13:13', 'Python', 9.0)
    (1504645994.7240334, '2017-09-05 11:13:14', 'Python', 9.0)
    (1504645995.7289774, '2017-09-05 11:13:15', 'Python', 3.0)
    (1504645996.7314699, '2017-09-05 11:13:16', 'Python', 7.0)
    
    (1504645987.6520224, '2017-09-05 11:13:07', 'Python', 0.0)
    (1504645988.661296, '2017-09-05 11:13:08', 'Python', 3.0)
    (1504645989.6734655, '2017-09-05 11:13:09', 'Python', 6.0)
    (1504645990.6875265, '2017-09-05 11:13:10', 'Python', 3.0)
    (1504645991.6941302, '2017-09-05 11:13:11', 'Python', 4.0)
    (1504645992.7065065, '2017-09-05 11:13:12', 'Python', 9.0)
    (1504645993.7204556, '2017-09-05 11:13:13', 'Python', 9.0)
    (1504645994.7240334, '2017-09-05 11:13:14', 'Python', 9.0)
    (1504645995.7289774, '2017-09-05 11:13:15', 'Python', 3.0)
    (1504645996.7314699, '2017-09-05 11:13:16', 'Python', 7.0)
    


```python

```


```python

```
