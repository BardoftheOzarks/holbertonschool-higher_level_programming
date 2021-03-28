#!/usr/bin/python3
'''
Lists all states in database hbtn_0e_0_usa that match user input
'''
if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect('localhost', argv[1], argv[2], argv[3])
    cur = db. cursor()

    cur.execute("SELECT cities.id, cities.name, states.name\
    FROM cities INNER JOIN states on states.id=cities.state_id\
    ORDER BY cities.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print("({}, '{}', '{}')".format(row[0], row[1], row[2]))
    cur.close()
    db.close()
