#!/usr/bin/python3
"""
Lists all cities of a given state from the database.
Results are displayed in ascending order by cities.id.
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
        "SELECT cities.name "
        "FROM cities "
        "JOIN states "
        "ON cities.state_id = states.id "
        "WHERE BINARY states.name = %s "
        "ORDER BY cities.id ASC",
        (sys.argv[4],)
        )

    rows = cur.fetchall()
    cities = [row[0] for row in rows]
    print(", ".join(cities))

    cur.close()
    conn.close()
