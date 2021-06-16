import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

nama = input('Masukkan nama : ')
nim = int(input('Masukkan nim : '))
prodi = input('Masukkan prodi : ')
jk = input('Masukkan jenis kelamin (L/P) : ')

sql = f"INSERT INTO mahasiswa VALUES({nim},'{nama}','{prodi}','{jk}')"

c.execute(sql)
conn.commit()

c.close()
conn.close()