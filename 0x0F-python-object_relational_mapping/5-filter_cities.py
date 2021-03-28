#!/usr/bin/python3
'''
Lists all states in database hbtn_0e_0_usa that match user input
'''
if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect('localhost', argv[1], argv[2], argv[3])
    cur = db. cursor()

    cur.execute("SELECT cities.name, states.name FROM cities INNER JOIN states on states.id=cities.state_id ORDER BY cities.id ASC")
    rows = cur.fetchall()
    cities = []
    for row in rows:
        if row[1] == argv[4]:
            cities.append(row[0])

    print('%s'% ', '.join(map(str, cities)))
    cur.close()
    db.close()
