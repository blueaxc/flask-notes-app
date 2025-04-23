
from flask import Flask, request, render_template
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ['DB_HOST'],
        dbname=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASS']
    )
    return conn

@app.route('/', methods=['GET', 'POST'])
def home():
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        if request.method == 'POST':
            note = request.form['note']
            cur.execute('INSERT INTO notes (title) VALUES (%s);', (note,))
            conn.commit()

        cur.execute('SELECT title, created_at FROM notes ORDER BY created_at DESC;')
        notes = cur.fetchall()

        cur.close()
        conn.close()
        
        return render_template('index.html', notes=notes)

    except Exception as e:
        return f'Erorr: {e}', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)