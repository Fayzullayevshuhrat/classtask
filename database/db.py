import psycopg2

def add_user(name, age, phone, referal=None):
    conn = psycopg2.connect("dbname=postgres user=postgres password='    ' host=localhost")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (name, age, phone, referal) VALUES (%s, %s, %s, %s);",
        (name, age, phone, referal)
    )

    conn.commit()
    cursor.close()
    conn.close()
