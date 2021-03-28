#!/usr/bin/python3
'''
Lists all states in database hbtn_0e_0_usa that match user input
'''
if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect('localhost', argv[1], argv[2], argv[3])
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name='{}'\
    ORDER BY states.id ASC".format(argv[4]))
    rows = cur.fetchall()
    for row in rows:
        if (row[1] == argv[4]):
            print(row)
    cur.close()
    db.close()
