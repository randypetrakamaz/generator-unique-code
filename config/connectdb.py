import psycopg2

# Konfigurasi database
DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "admin"

def get_db_connection():
    """
    Membuka dan mengembalikan koneksi ke database PostgreSQL
    """
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn