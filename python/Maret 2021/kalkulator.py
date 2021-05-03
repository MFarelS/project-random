import os
width = os.get_terminal_size().columns
def output(nilai1,operator,nilai2,hasil):
    print(" Hasil ".center(width,"="))
    print("         ",nilai1,operator,nilai2,"=",hasil)

def tambah(nilai1,operator, nilai2):
    hasil = nilai1+nilai2
    output(nilai1, operator, nilai2, hasil)

def kurang(nilai1,operator, nilai2):
    hasil = nilai1-nilai2
    output(nilai1, operator, nilai2, hasil)

def kali(nilai1,operator, nilai2):
    hasil = nilai1*nilai2
    output(nilai1, operator, nilai2, hasil)

def bagi(nilai1,operator, nilai2):
    nilai1 = float(nilai1)
    nilai2 = float(nilai2)
    hasil = nilai1/nilai2
    hasil = round(hasil,2)
    output(nilai1, operator, nilai2, hasil)

def mod(nilai1,operator, nilai2):
    hasil = nilai1%nilai2
    output(nilai1, operator, nilai2, hasil)

def getNilai2(nilai1,operator):
    nilai2 = input("          Masukkan nilai 2           = ")
    if(nilai2.isdigit()):
        nilai2 = int(nilai2)
        if(operator == "+"):
            tambah(nilai1,operator,nilai2)
        elif(operator == "-"):
            kurang(nilai1,operator,nilai2)
        elif(operator == "*"):
            kali(nilai1,operator,nilai2)
        elif(operator == "/"):
            bagi(nilai1,operator,nilai2)
        elif(operator == "%"):
            mod(nilai1,operator,nilai2)
    else:
        os.system("clear")
        print("Input tidak valid!")
        getNilai1()

def getOperator(nilai1):
    operator = input("          Pilih operator (+,-,*,/,%) = ")
    if operator in {"+","-","*","/","%"}:
        getNilai2(nilai1,operator)
    else:
        os.system("clear")
        print("Operator tidak valid!")
        getNilai1()

def getNilai1():
    print(" Kalkulator ".center(width,"="))
    nilai1 = input("          Masukkan nilai 1           = ")
    if(nilai1.isdigit()):
        nilai1 = int(nilai1)
        getOperator(nilai1)
    else:
        os.system("clear")
        print("Input tidak valid!")
        getNilai1()

getNilai1()
