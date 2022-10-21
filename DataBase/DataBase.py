import sqlite3
 
try:
    conn = sqlite3.connect('zbior.db')
except:
    print ('Błąd połączenia z bazą danych PostgreSQL.')

cursor = conn.cursor()
#conn.commit()

cursor.execute("CREATE TABLE IF NOT EXISTS programista (id SERIAL PRIMARY KEY, imie VARCHAR(80), nazwisko VARCHAR(80));")
cursor.execute("INSERT INTO programista(imie, nazwisko) VALUES ('Andrzej', 'Kowalski')")
cursor.execute("SELECT * FROM programista")
records = cursor.fetchall()


for record in records:
    print (record)

