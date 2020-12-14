#!/usr/bin/python3
'''Lists all states starting with N from database hbtn_0e_0_usa'''


import MySQLdb
from sys import argv

if __name__ == '__main__':
    my_host = 'localhost'
    db = MySQLdb.connect(host=my_host, port=3306,
                         user=argv[1], passwd=argv[2],
                         db=argv[3])
    if len(argv) == 6:
        state = '{} {}'.format(argv[4], argv[5])
    else:
        state = argv[4]
    c = db.cursor()
    c.execute('SELECT cities.name, states.name FROM cities \
    INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC')
    rows = c.fetchall()
    result = ''
    count = 0
    for row in rows:
        if row[1] == state:
            if count > 0:
                result += ', '
            result += row[0]
            count += 1
    print(result)
    c.close()
    db.close()
