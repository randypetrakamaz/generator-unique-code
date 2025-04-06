from config.connectdb import get_db_connection

class UniqueCodes:
    @staticmethod
    def create_codes(username, email):
        # Fungsi untuk menambahkan user ke database
        conn = get_db_connection()
        cur = conn.cursor()
        
        try:
            cur.execute(
                "INSERT INTO unique_codes (username, email) VALUES (%s, %s)", 
                (username, email)
            )
            conn.commit()
        except Exception as e:
            print(f"Error: {e}")
            conn.rollback()
        finally:
            cur.close()
            conn.close()

    @staticmethod
    def get_all_codes():
        conn = get_db_connection()
        cur = conn.cursor()
        
        try:
            cur.execute("SELECT * FROM test_table")
            datas = cur.fetchall()
        except Exception as e:
            print(f"Error: {e}")
            datas = []
        finally:
            cur.close()
            conn.close()
        
        return datas
