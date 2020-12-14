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
    c.execute('SELECT * FROM states ORDER BY id ASC')
    rows = c.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)
    c.close()
    db.close()
