import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import DB
import DAO

class DatabaseManager:
    def __init__(self, db_name='database.db'):
        self.db_name = db_name

    def execute_query(self, query, params=None):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            rows = cursor.fetchall()
            conn.commit()
            return rows
        except sqlite3.Error as e:
            print("Error executing query:", e)
            return None
        finally:
            conn.close()

class LoginWindow(tk.Tk):
    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self.title("Login")
        
        self.username_label = ttk.Label(self, text="Username:")
        self.username_entry = ttk.Entry(self)
        self.password_label = ttk.Label(self, text="Password:")
        self.password_entry = ttk.Entry(self, show="*")
        self.login_button = ttk.Button(self, text="Login", command=self.login)

        self.username_label.grid(row=0, column=0, padx=10, pady=5)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)
        self.password_label.grid(row=1, column=0, padx=10, pady=5)
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)
        self.login_button.grid(row=2, columnspan=2, padx=10, pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user_data = self.db_manager.execute_query("SELECT * FROM accounts WHERE username=? AND password=?", (username, password))
        if user_data:
            role = user_data[0][3]
            if role == 'parent':
                parent_main_window = ParentMainWindow(self, username)
                parent_main_window.mainloop()
            elif role == 'child':
                child_main_window = ChildMainWindow(self, username)
                child_main_window.mainloop()
        else:
            messagebox.showerror("Error", "Invalid username or password.")

class ParentMainWindow(tk.Toplevel):
    def __init__(self, parent, username):
        super().__init__(parent)
        self.title("Parent Main Page")
        self.parent = parent
        self.username = username

        self.mission_list_button = ttk.Button(self, text="View Mission List", command=self.view_mission_list)
        self.logout_button = ttk.Button(self, text="Logout", command=self.logout)

        self.mission_list_button.pack(padx=10, pady=5)
        self.logout_button.pack(padx=10, pady=5)

    def view_mission_list(self):
        # View mission list logic
        pass

    def logout(self):
        self.destroy()
        self.parent.deiconify()

class ChildMainWindow(tk.Toplevel):
    def __init__(self, parent, username):
        super().__init__(parent)
        self.title("Child Main Page")
        self.parent = parent
        self.username = username

        self.mission_list_button = ttk.Button(self, text="View Mission List", command=self.view_mission_list)
        self.logout_button = ttk.Button(self, text="Logout", command=self.logout)

        self.mission_list_button.pack(padx=10, pady=5)
        self.logout_button.pack(padx=10, pady=5)

    def view_mission_list(self):
        # View mission list logic
        pass

    def logout(self):
        self.destroy()
        self.parent.deiconify()

# 사용 예시
if __name__ == "__main__":
    db_manager = DatabaseManager()
    login_window = LoginWindow(db_manager)
    login_window.mainloop()
