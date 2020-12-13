#!/usr/bin/python3
'''Lists all states from database hbtn_0e_0_usa'''


if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2],
                         db=argv[3])
    c = db.cursor()
    c.execute('SELECT id, name FROM states ORDER BY states.id ASC')
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
