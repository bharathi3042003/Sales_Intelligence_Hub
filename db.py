import psycopg2

def get_connection():
    return psycopg2.connect(
        host="dpg-d83fol67r5hc73boh4hg-a.singapore-postgres.render.com",
        database="salemanagementdb_hcwt",
        user="jayabharathi",
        password="8HrtDMdBhMBiqmwo7wpWiQbjSmvokIO5",
        port="5432"
    )