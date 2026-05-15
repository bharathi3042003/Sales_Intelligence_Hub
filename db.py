import psycopg2

def get_connection():
    return psycopg2.connect(
        host="dpg-d7d4vvq8qa3s73b10540-a.singapore-postgres.render.com",
        database="salemanagementdb_flpa",
        user="jayabharathi",
        password="GRGzARJJc8kpCYs3RdAeMrMZdOSTCiJ2",
        port="5432"
    )