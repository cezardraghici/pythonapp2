import sqlite3
import pandas as pd
from tkinter.filedialog import askopenfilename, asksaveasfilename

def connect():
    conn=sqlite3.connect("curs_valutar.db")
    return conn

def create_table():
    conn=connect()
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS curs_valutar (id INTEGER PRIMARY KEY AUTOINCREMENT, nume_banca text, moneda text, cumpara text, vinde text, cr_data text)")
    conn.commit()
    conn.close()

def insert(nume_banca,moneda,cumpara,vinde,cr_data):
    conn=connect()
    cur=conn.cursor()
    cur.execute("INSERT INTO curs_valutar (nume_banca,moneda,cumpara,vinde,cr_data) VALUES (?,?,?,?,?)",(nume_banca,moneda,cumpara,vinde,cr_data))
    conn.commit()
    conn.close()

def view(variable):
    conn=connect()
    cur=conn.cursor()
    cur.execute("SELECT nume_banca,cumpara,vinde FROM curs_valutar where moneda like ?",('%'+variable+'%',))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete():
    conn=connect()
    cur=conn.cursor()
    cur.execute("DELETE FROM curs_valutar")
    conn.commit()
    conn.close()

def data():
    conn=connect()
    cur=conn.cursor()
    cur.execute("Select max(date(cr_data)) from curs_valutar")
    row=cur.fetchall()
    conn.close()
    return row

def drop():
    conn=connect()
    cur=conn.cursor()
    cur.execute("DROP TABLE curs_valutar")
    conn.commit()
    conn.close()

#drop()
create_table()
