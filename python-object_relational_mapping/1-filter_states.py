#!/usr/bin/python3
"""
Lists all states from the database whose name starts with 'N'.
Results are displayed in ascending order by id.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
        charset="utf8"
        )
    cur = conn.cursor()

    cur.execute(
        "SELECT * "
        "FROM states "
        "WHERE BINARY name LIKE 'N%' "
        "ORDER BY id ASC "
        )

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
