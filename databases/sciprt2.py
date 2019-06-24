import psycopg2


def create_table():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def inset(item, quantity, price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store  VALUES (%s, %s, %s)", (item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store where item=%s", (item,))
    conn.commit()
    conn.close()


def update(quantity, price, item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s where item=%s", (quantity, price, item))
    conn.commit()
    conn.close()

# inset("Water Glassm", 10, 5)
# delete("Wine Glass")
# update(15, 7.0, "Water Glassm")
# print(view())


# create_table()
# inset("Orange", 10, 15)
print(view())
# delete("Apple")
update(20,15.0, "Orange")