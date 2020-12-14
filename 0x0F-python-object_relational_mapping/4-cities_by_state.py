#!/usr/bin/python3
'''Lists all states starting with N from database hbtn_0e_0_usa'''


import MySQLdb
from sys import argv

if __name__ == '__main__':
    my_host = 'localhost'
    db = MySQLdb.connect(host=my_host, port=3306,
                         user=argv[1], passwd=argv[2],
                         db=argv[3])
    c = db.cursor()
    c.execute('SELECT cities.id, cities.name, states.name FROM cities \
    INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC')
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
