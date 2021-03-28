#!/usr/bin/python3
'''
Lists all states in database hbtn_0e_0_usa starting with N
'''
if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect('localhost', argv[1], argv[2], argv[3])
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        if (row[1][0] is 'N'):
            print(row)
    cur.close()
    db.close()
