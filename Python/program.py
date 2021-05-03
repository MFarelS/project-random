import os
os.system("clear")
# function
def get_nama():
    nama = input("Masukkan nama = ")
    return nama
def get_gol():
    gol = input("Masukkan golongan (A/B/C) = ")
    return gol
def get_gapok(gol):
    if gol == "A":
        gapok = 600000
    elif gol == "B":
        gapok = 800000
    elif gol == "C":
        gapok = 1000000
    return gapok
def get_tunja(gol):
    if gol == "A":
        tunja = 50000
    elif gol == "B":
        tunja = 70000
    elif gol == "C":
        tunja = 120000
    return tunja
def get_trans(gol):
    if gol == "A":
        trans = 1000000
    elif gol == "B":
        trans = 2000000
    elif gol == "C":
        trans = 3000000
    return trans
def get_prosen(gol):
    if gol == "A":
        prosen = 0.02
    elif gol == "B":
        prosen = 0.03
    elif gol == "C":
        prosen = 0.04
    return prosen
def get_gatot(gol):
    gatot = get_gapok(gol) + get_tunja(gol) + get_trans(gol)
    return gatot
def get_pajak(gol):
    pajak = get_gatot(gol) * get_prosen(gol)
    return pajak
def get_gaber(gol):
    gaber = get_gatot(gol) - get_pajak(gol)
    return gaber
def output(nama,gol):
    print('===========Output=============')
    print('Nama Karyawan :',nama)
    print('Golongan      :',gol)
    print('Gaji Pokok    : Rp',get_gapok(gol))
    print('Tunjangan     : Rp',get_tunja(gol))
    print('Transport     : Rp',get_trans(gol))
    print('Pajak         : Rp',int(get_pajak(gol)))
    print('Gaji Bersih   : Rp',int(get_gaber(gol)))

# main program
nama = get_nama()
gol = get_gol()
output(nama,gol)
