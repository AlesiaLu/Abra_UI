import psycopg2 as ps
connection = ps.connect(
    host='172.212.108.64',
    user='heJq1mnbruN',
    password='Ul1mn7n2lMlwNuHHe',
    database='postgres'
)


def select_all(sql_query: str):
    cursor = connection.cursor()
    cursor.execute(sql_query)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data
