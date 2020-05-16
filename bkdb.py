import sqlite3
import pandas as pd
from tkinter.filedialog import askopenfilename, asksaveasfilename





def connect():
    conn=sqlite3.connect("curs_valutar.db")
    return conn

def create_table():
    conn=connect()
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS curs_valutar (id INTEGER PRIMARY KEY AUTOINCREMENT, nume_banca text, moneda text, cumpara text, vinde text)")
    conn.commit()
    conn.close()

def insert(nume_banca,moneda,cumpara,vinde):
    conn=connect()
    cur=conn.cursor()
    cur.execute("INSERT INTO curs_valutar (nume_banca,moneda,cumpara,vinde) VALUES (?,?,?,?)",(nume_banca,moneda,cumpara,vinde))
    conn.commit()
    conn.close()

def view_all():
    conn=connect()
    cur=conn.cursor()
    cur.execute("SELECT nume_banca,cumpara,vinde FROM curs_valutar")
    rows=cur.fetchall()
    conn.close()
    return rows

def view(variable):
    conn=connect()
    cur=conn.cursor()
    cur.execute("SELECT nume_banca,cumpara,vinde FROM curs_valutar where moneda=?",(variable,))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete():
    conn=connect()
    cur=conn.cursor()
    cur.execute("DELETE FROM curs_valutar")
    conn.commit()
    conn.close()

def drop():
   conn=connect()
   cur=conn.cursor()
   cur.execute("DROP TABLE curs_valutar")
   conn.commit()
   conn.close()


create_table()
