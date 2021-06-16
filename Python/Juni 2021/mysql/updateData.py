import sqlite3
from prettytable import PrettyTable

conn = sqlite3.connect('data.db')
c = conn.cursor()

nama = input("Masukkan nama orang yang akan diubah : ")

tabel = PrettyTable(['NIM','Nama','Prodi','JK'])

try:
    c.execute(f"SELECT * FROM mahasiswa WHERE nama like '%{nama}%'")
except:
    print("Data tidak ditemukan")


for row in c.fetchall():
    nim = row[0]
    nama = row[1]
    prodi = row[2]
    jk = row[3]
    tabel.add_row([nim,nama,prodi,jk])
print(tabel)
nama = input(f'Masukkan nama ({nama}): ')
prodi = input(f'Masukkan prodi ({prodi}) : ')
jk = input(f'Masukkan jenis kelamin (L/P) ({jk}) : ')

sql = f"UPDATE mahasiswa SET nama = '{nama}', prodi = '{prodi}', jk = '{jk}' WHERE nim = {nim}"
c.execute(sql)
conn.commit()

c.close()
conn.close()
