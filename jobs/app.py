import sqlite3
from flask import Flask, render_template, g

PATH = 'db/jobs/sqlite'

app = Flask('__name__')

def open_connnection():
    connection = getattr(g, 'connection', None)
    if connection == None:
        connection = g._connection = sqlite3.connect(PATH)
    connection.row_factory = sqlite3.Row
    return connection

def execute_sql(sql, values=(), commit=False, single=False):
    connection = open_connection()
    cursor = connnection.execute(sql, values)
    if commit == True:
        results = connection.commit()
    else:
        results = cursor.fetchone() if single else cursor.fetchall()

    cursor.close()
    return results        

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')