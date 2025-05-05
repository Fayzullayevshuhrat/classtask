import psycopg2

def add_user(name):
    conn = psycopg2.connect("dbname=postgres user=postgres password='    '")

    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO oka(name) VALUES ('{name}');")

    conn.commit()

    cursor.close()
    conn.close()