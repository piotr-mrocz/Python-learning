import sqlite3
 
try:
    conn = sqlite3.connect('zbior.sql')
except:
    print ('Błąd połączenia z bazą danych PostgreSQL.')

cursor = conn.cursor()
conn.commit()

cursor.execute("SELECT * FROM zbior")
records = cursor.fetchall()


for record in records:
    print (record)