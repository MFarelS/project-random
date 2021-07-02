import os, time
pin = 1234
while(True):
    mas = int(input("Masukkan PIN : "))
    if mas == pin:
        print("Benar")
        break
    else:
        print("Salah")
        time.sleep(1)
        os.system("clear")
        continue
