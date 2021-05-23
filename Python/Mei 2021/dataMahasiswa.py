import os
from colored import fg, attr

def clear():
  os.system("clear")

class Mahasiswa():
  def __init__(self,nama,nim):
    self.nama = nama
    self.nim = nim
    
  daftarMhs = {
    {
      'nama' : self.nama,
      'nim' : self.nim
    }
  }

class App:
  def register(self):
    str = f"""
      Register \n\n
      {fg(2)}{attr(1)}>{attr(0)} """
    nama = input("""
      Nama : """)
    nim = input("""
      NIM  : """)
    mhs = Mahasiswa(nama,nim)
    clear()
    print(f"""
      {fg(2)}{attr(1)}Registrasi Sukses!
      Selamat datang {mhs.daftarMhs.get(nama)}{attr(0)} """)
    self.welcome()

  def welcome(self):
    str = f"""
      Selamat datang di halaman utama \n\n
      1. Login \n
      2. Register \n\n
      {fg(2)}{attr(1)}>{attr(0)} """
    choice = int(input(str))
    # self.choice = choice
    if choice == 1:
      pass
    elif choice == 2:
      clear()
      self.register()
    
app = App()
app.welcome()