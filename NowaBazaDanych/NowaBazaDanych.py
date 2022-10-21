import sqlite3
 
try:
    conn = sqlite3.connect('baza_danych.db')
except:
    print ('Błąd połączenia z bazą danych PostgreSQL.')
 
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS programista (id SERIAL PRIMARY KEY, imie VARCHAR(80), nazwisko VARCHAR(80));")
cursor.execute("INSERT INTO programista(imie, nazwisko) VALUES ('Andrzej', 'Kowalski')")
cursor.execute("INSERT INTO programista(imie, nazwisko) VALUES ('Jan', 'Nowak')")
conn.commit()
 
cursor = conn.cursor()
try:
    cursor.execute("SELECT * FROM programista")
    records = cursor.fetchall()
except:
    print ('Błąd połączenia z bazą danych PostgreSQL.')
 
for record in records:
    print (record)