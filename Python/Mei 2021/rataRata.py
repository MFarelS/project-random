import os
def clear():
  os.system("clear")
print("Program Penghitung Rata-Rata")
jumlah = 0
total = 1
while True:
  angka = int(input(f"Masukkan angka ke-{total} : "))
  if angka == 9999:
    break
  total += 1
  jumlah += angka

rata = jumlah / (total - 1)
print("Rata-rata :",rata)