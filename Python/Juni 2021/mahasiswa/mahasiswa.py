import sqlite3, os
from prettytable import PrettyTable
conn = sqlite3.connect('mahasiswa.db')
c = conn.cursor()

class Tabel:
    def showData(self):
        self.tabel = PrettyTable(["NIM","Nama","Prodi","Alamat"])
        c.execute("SELECT * FROM mahasiswa")
        for row in c.fetchall():
            self.nim = row[0]
            self.nama = row[1]
            self.prodi = row[2]
            self.alamat = row[3]
            self.tabel.add_row([self.nim, self.nama, self.prodi, self.alamat])
        print(self.tabel)
        self.tabel.clear_rows()

    def insertData(self):


    def menu(self):
        print("""1. Masukkan data
2. Ubah data
3. Hapus data
""")
        choice = int(input("Pilih menu : "))
        if choice == 2:
            os.system("clear")
            self.nim = int(input("Masukkan NIM : "))
            self.nama = input("Masukkan nama : ")
            self.prodi = input("Masukkan prodi : ")
            self.alamat = input("Masukkan alamat : ")
            self.insertData()
        else:
            print("Pilihan tidak valid!")

obj = Tabel()
obj.showData()
obj.menu()

c.close()
conn.close()
