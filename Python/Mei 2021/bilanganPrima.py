import os
def clear():
  os.system("clear")
while(True):
  try:
    angka = int(input("Masukkan angka : "))
  except:
    clear()
    print("Input tidak valid!")
  else:
    clear()
    if angka > 1:
      for i in range(2,angka):
        if angka % i == 0:
          clear()
          print(f"{angka} bukan bilangan prima")
        else:
          print(f"{angka} adalah bilangan prima")
          break
          break
    else:
      clear()
      print(f"{angka} bukan bilangan prima")
    if angka == 9999:
      break