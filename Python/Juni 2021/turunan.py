import os
def tampilan(x):
    print("PROGRAM PENGHITUNG TURUNAN FUNGSI")
    print(f"f(x) = {x}")

def turunan(k,v,p):
    if v=='' :
        k=0
        p=0
        h= "0"
    else :
        k = k * p
        p = p - 1
        h = f"{k}{v}^{p}"
    return h

tampilan("")

k = int(input("Masukkan konstanta : ") or 0)
os.system("clear")
if k == 0:
    tampilan("")
else:
    tampilan(k)

v = input("Masukkan variabel : ")
if v != '':
    os.system("clear")
    if k == 0:
        tampilan(f"{v}")
    else:
        tampilan(f"{k}{v}")
    p = int(input("Masukkan pangkat : ") or 1)
else:
    os.system("clear")
    p = 1
    if v == '':
        tampilan(f"{k}{v}")
    else:
        tampilan(f"{k}{v}^{p}")

h = turunan(k,v,p)
if h[-2:] == "^1":
    h = h.replace("^1","")

print(f"f'(x) = {h}")
