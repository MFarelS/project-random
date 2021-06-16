import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

sql = "CREATE TABLE IF NOT EXISTS mahasiswa( \
      nim Integer(9) PRIMARY KEY, \
      nama Text(30), \
      prodi Text(30), \
      jk Text(1))"

c.execute(sql)

c.close()
conn.close()