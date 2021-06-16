# import module
import sqlite3, os
from prettytable import PrettyTable, from_db_cursor

# koneksi ke database
conn = sqlite3.connect('db/mahasiswa.db')

# membuat variabel cursor
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS mahasiswa(
nim integer not null primary key,
nama text,
prodi text,
alamat text);""")

# kelas tabel
class Tabel:
    # method menampilkan data
    def showData(self):
        self.tabel = PrettyTable()
        c.execute("SELECT * FROM mahasiswa ORDER BY nim ASC")
        self.tabel = from_db_cursor(c)
        self.tabel.field_names = ["NIM","Nama","Prodi","Alamat"]
        print("====================== DATA MAHASISWA UNIBBA ======================")
        print(self.tabel)
        self.tabel.clear_rows()

    # method memasukkan data
    def insertData(self, nim, nama, prodi, alamat):
        c.execute(f"INSERT INTO mahasiswa VALUES( \
                    {nim}, \
                    '{nama}', \
                    '{prodi}', \
                    '{alamat}' \
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
        choice = input("Pilih menu : ")
        if choice.isdigit():
            choice = int(choice)
        else:
            os.system("clear")
            print("Pilihan tidak valid!")
            self.showData()
            self.menu()
        # insert data
        if choice == 1:
            os.system("clear")
            while(True):
                self.showData()
                print("======================= INPUT DATA MAHASISWA ======================")
                nim = input("Masukkan NIM    : ")
                if nim.isdigit():
                    nim = int(nim)
                else:
                    os.system("clear")
                    print("Input tidak valid! NIM harus berupa bilangan bulat")
                    continue
      
                nama = input("Masukkan nama   : ") or "-"
                prodi = input("Masukkan prodi  : ") or "-"
                alamat = input("Masukkan alamat : ") or "-"
                try:
                    self.insertData(nim, nama, prodi, alamat)
                    os.system("clear")
                    print("Input data berhasil!")
                except:
                    os.system("clear")
                    print("Input data gagal!")
                self.showData()
                self.menu()
                break
        # update data
        elif choice == 2:
            os.system("clear")
            while(True):
                self.showData()
                chooseNim = input("Masukkan NIM data yang akan diubah: ")
                if chooseNim.isdigit():
                    chooseNim = int(chooseNim)
                else:
                    os.system("clear")
                    print("Input tidak valid! NIM harus berupa bilangan bulat")
                    continue
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
                        print("====================== UPDATE DATA MAHASISWA ======================")
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
                break
        # delete data   
        elif choice == 3:
            os.system("clear")
            while(True):
                self.showData()
                chooseNim = input("Masukkan NIM data yang akan dihapus: ")
                if chooseNim.isdigit():
                    chooseNim = int(chooseNim)
                else:
                    os.system("clear")
                    print("Input tidak valid! NIM harus berupa bilangan bulat")
                    continue
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
                        print("====================== DELETE DATA MAHASISWA ======================")
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
                        else:
                            os.system("clear")
                            print("Pilihan tidak valid!")
                        self.showData()
                        self.menu()
                break
        # keluar dari program
        elif choice == 4:
            print("========================= PROGRAM SELESAI =========================")
            quit()
        # input error
        else:
            os.system("clear")
            print("Pilihan tidak valid!")
            self.showData()
            self.menu()

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
