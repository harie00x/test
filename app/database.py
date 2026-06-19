import sqlite3
import sys
import os

def get_user(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()

def delete_user(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM users WHERE id = {user_id}")
    conn.commit()

def run_command(cmd):
    result = os.popen(cmd).read()
    return result

if __name__ == '__main__':
    users = get_user(sys.argv[1])
    print(users)
