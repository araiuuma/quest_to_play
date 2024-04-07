import sqlite3

class DatabaseManager:
    def __init__(self, db_name='database.db'):
        self.db_name = db_name

    def create_tables(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        try:
            # 계정 테이블 생성
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                role TEXT NOT NULL
            )
            ''')

            # 미션 테이블 생성
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS missions (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                reward_time INTEGER NOT NULL,
                clear_condition TEXT NOT NULL
            )
            ''')

            # 사용시간 테이블 생성
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS time_usage (
                id INTEGER PRIMARY KEY,
                user_id INTEGER NOT NULL,
                used_time INTEGER NOT NULL,
                remaining_time INTEGER NOT NULL,
                FOREIGN KEY(user_id) REFERENCES accounts(id)
            )
            ''')

            conn.commit()
            print("Tables created successfully.")
        except sqlite3.Error as e:
            print("Error creating tables:", e)
        finally:
            conn.close()

    def execute_query(self, query, params=None):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            rows = cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            print("Error executing query:", e)
            return None
        finally:
            conn.close()
