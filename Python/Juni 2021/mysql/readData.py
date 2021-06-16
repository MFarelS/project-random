import sqlite3
from prettytable import PrettyTable

conn = sqlite3.connect('data.db')
c = conn.cursor()

tabel = PrettyTable(['NIM','Nama','Prodi','JK'])
sql = "SELECT * FROM mahasiswa ORDER BY nim ASC"

c.execute(sql)
for row in c.fetchall():
  nim = row[0]
  nama = row[1]
  prodi = row[2]
  jk = row[3]
  tabel.add_row([nim,nama,prodi,jk])
print(tabel)

c.close()
conn.close()
