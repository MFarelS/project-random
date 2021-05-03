import time
import os
green = "\033[1;32;40m"
red = "\033[1;31;40m"
blue = "\033[1;34;40m"
bold = "\033[1;1;40m"
nomor = input(green + f"Masukkan nomor target = {blue}")
jumlah = int(input(f"{green}Masukkan jumlah trojan = {blue}"))
print("")
for i in range(0, jumlah):
    print(f"{green}Success send trojan to: {blue}{nomor}{green} [{red}{i + 1}{green}]")
    time.sleep(0.05)

print(f"\n{bold}Trojan telah berhasil dikirim")
