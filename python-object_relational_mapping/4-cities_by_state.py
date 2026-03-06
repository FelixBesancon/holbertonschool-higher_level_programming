#!/usr/bin/python3
"""
Lists all cities from the database with their corresponding state name.
Results are sorted by cities.id in ascending order.
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
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states "
        "ON cities.state_id = states.id "
        "ORDER BY cities.id ASC "
        )

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
