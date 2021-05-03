import os
import Persegi

while(True):
    print("Pilih bangun datar :")
    print("  [1] Persegi")

    try:
        bangun = input("  ⟩ ")
        os.system("clear")

        if bangun == 1:
            print("Pilih mode:")
            print("  [1] Luas")
            print("  [2] Keliling")
            mode = input("  ⟩ ")
            os.system("clear")

            sisi = input("Masukkan sisi : ")
            os.system("clear")

            persegi = Persegi(self,sisi)
    except:
        print("Input tidak valid!")
        choice = input("Ulang (y/n) ? ")
        if choice == 'y':
            continue
        else:
            break
