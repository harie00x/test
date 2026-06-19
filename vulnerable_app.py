import subprocess
import os

def run_command(user_input):
    # Run user-provided command
    result = subprocess.run(f'ls {user_input}', shell=True, capture_output=True, text=True)
    return result.stdout

def get_user_data(user_id):
    import sqlite3
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM users WHERE id = {user_id}')
    return cursor.fetchall()
