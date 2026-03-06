#!/usr/bin/python3
"""
Displays all states from the database whose name matches the user input.
Results are sorted in ascending order by id.
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

    query = (
        "SELECT id, name "
        "FROM states "
        "WHERE name = '{}' "
        "ORDER BY id ASC"
    ).format(sys.argv[4])

    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
