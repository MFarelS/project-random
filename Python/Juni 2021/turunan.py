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
k = input("Masukkan konstanta : ")
os.system("clear")
tampilan(k)
v = input("Masukkan variabel : ")
os.system("clear")
tampilan(f"{k}{v}")
p = input("Masukkan pangkat : ")
os.system("clear")
tampilan(f"{k}{v}^{p}")

h = turunan(k,v,p)
if h[-2:] == "^1":
    h = h.replace("^1","")

print(f"f'(x) = {h}")
