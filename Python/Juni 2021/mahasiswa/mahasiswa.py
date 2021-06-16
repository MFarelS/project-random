# import module
import sqlite3, os
from prettytable import PrettyTable

# koneksi ke database
conn = sqlite3.connect('mahasiswa.db')

# membuat variabel cursor
c = conn.cursor()

# kelas tabel
class Tabel:
    # method menampilkan data
    def showData(self):
        self.tabel = PrettyTable(["NIM","Nama","Prodi","Alamat"])
        c.execute("SELECT * FROM mahasiswa ORDER BY nim ASC")
        for row in c.fetchall():
            self.nim = row[0]
            self.nama = row[1]
            self.prodi = row[2]
            self.alamat = row[3]
            self.tabel.add_row([self.nim, self.nama, self.prodi, self.alamat])
        print(self.tabel)
        self.tabel.clear_rows()

    # method memasukkan data
    def insertData(self, nim, nama, prodi, alamat):
        c.execute(f"INSERT INTO mahasiswa VALUES( \
                    {nim}, \
                    '{nama}', \
                    '{prodi}', \
                    '{alamat}' \
    def updateData(self, nim, nama, prodi, alamat):
        c.execute(f"UPDATE mahasiswa SET \
                    nama = '{nama}', \
                    prodi = '{prodi}', \
                    alamat = '{alamat}' \
                    WHERE nim = {nim} \
                  ")
        conn.commit()
                  )")
        conn.commit()

    # method mengubah data
    def updateData(self, nim, nama, prodi, alamat):
        c.execute(f"UPDATE mahasiswa SET \
                    nama = '{nama}', \
                    prodi = '{prodi}', \
                    alamat = '{alamat}' \
                    WHERE nim = {nim} \
                  ")
        conn.commit()

    # method menghapus data
    def deleteData(self, nim):
        c.execute(f"DELETE FROM mahasiswa \
                    WHERE nim = {nim} \
                  ")
        conn.commit()

    # method menampilkan menu
    def menu(self):
        print("""1. Masukkan data
2. Ubah data
3. Hapus data
4. Keluar
""")
        choice = int(input("Pilih menu : "))
        # insert data
        if choice == 1:
            os.system("clear")
            self.showData()
            print("Input Data Mahasiswa \n")
            nim = int(input("Masukkan NIM    : "))
            nama = input("Masukkan nama   : ")
            prodi = input("Masukkan prodi  : ")
            alamat = input("Masukkan alamat : ")
            try:
                self.insertData(nim, nama, prodi, alamat)
                os.system("clear")
                print("Input data berhasil!")
            except:
                os.system("clear")
                print("Input data gagal!")
            self.showData()
            self.menu()
        # update data
        elif choice == 2:
            chooseNim = int(input("Masukkan NIM data yang akan diubah: "))
            c.execute(f"SELECT COUNT(*) FROM mahasiswa WHERE nim LIKE '%{chooseNim}%'")
            result = c.fetchone()
            if result[0] == 0:
                os.system("clear")
                print("NIM tidak ditemukan!")
                self.showData()
                self.menu()
            else:
                c.execute(f"SELECT * FROM mahasiswa WHERE nim LIKE '%{chooseNim}%'")
                for row in c.fetchall():
                    nim = row[0]
                    nama = row[1]
                    prodi = row[2]
                    alamat = row[3]
                    os.system("clear")
                    nama = input(f"Masukkan nama ({nama}) : ") or nama
                    prodi = input(f"Masukkan prodi ({prodi}) : ") or prodi
                    alamat = input(f"Masukkan alamat ({alamat}) : ") or alamat
                    try:
                        self.updateData(nim, nama, prodi, alamat)
                        os.system("clear")
                        print("Update data berhasil!")
                    except:
                        os.system("clear")
                        print("Update data gagal!")
                    self.showData()
                    self.menu()
        # delete data   
        elif choice == 3:
            chooseNim = int(input("Masukkan NIM data yang akan dihapus: "))
            c.execute(f"SELECT COUNT(*) FROM mahasiswa WHERE nim LIKE '%{chooseNim}%'")
            result = c.fetchone()
            if result[0] == 0:
                os.system("clear")
                print("NIM tidak ditemukan!")
                self.showData()
                self.menu()
            else:
                c.execute(f"SELECT * FROM mahasiswa WHERE nim LIKE '%{chooseNim}%' LIMIT 1")
                for row in c.fetchall():
                    os.system("clear")
                    nim = row[0]
                    nama = row[1]
                    prodi = row[2]
                    alamat = row[3]
                    self.tabel = PrettyTable(["NIM","Nama","Prodi","Alamat"])
                    c.execute(f"SELECT * FROM mahasiswa WHERE nim = {nim}")
                    for row in c.fetchall():
                        self.nim = row[0]
                        self.nama = row[1]
                        self.prodi = row[2]
                        self.alamat = row[3]
                        self.tabel.add_row([self.nim, self.nama, self.prodi, self.alamat])
                    print(self.tabel)
                    self.tabel.clear_rows()
                    choice = input("Apakah anda yakin akan menghapus data ini? (y/n) : ")
                    if choice.lower() == 'y':
                        self.deleteData(nim)
                        os.system("clear")
                        print("Delete data berhasil!")
                    elif choice.lower() == 'n':
                        os.system("clear")
                        print("Proses hapus dibatalkan!")
                    self.showData()
                    self.menu()
        # keluar dari program
        elif choice == 4:
            quit()
        # input error
        else:
            print("Pilihan tidak valid!")

# membuat objek dari kelas tabel
obj = Tabel()

# menampilkan data
obj.showData()

# menampilkan menu
obj.menu()

# menutup cursor
c.close()

# menutup koneksi database
conn.close()
