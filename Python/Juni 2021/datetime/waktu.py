from datetime import datetime
import os, time

def showTime():
    now = datetime.today()
    dt = now.strftime("%d/%m/%Y %H:%M:%S")
    print(f"[{dt}]", end=" ")

while True:
    showTime()
    nama = input("Masukkan nama : ")
    showTime()
    nim = input("Masukkan NIM  : ")

    if not nama.isdigit() and nim.isdigit():
        showTime()
        print("Input success!")
        break
    else:
        showTime()
        print("Input failed!")
