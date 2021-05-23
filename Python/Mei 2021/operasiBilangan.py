import os
from colored import fg, bg, attr

def clear():
  os.system("clear")
  
def header():
  print(f"{attr(1)}    Program Operasi Bilangan dengan Python 3{attr(0)} \n")

class Kalkulator:
  def __init__(self,bil1,bil2):
    self.bil1 = bil1
    self.op = op
    self.bil2 = bil2
    
  def tambah(self):
    print(f"    Hasil : {fg(4)}{self.bil1}{attr(0)} + {fg(4)}{self.bil2}{attr(0)} = {fg(2)}{attr(1)}{self.bil1 + self.bil2}{attr(0)}")
  
  def kurang(self):
    print(f"    Hasil : {fg(4)}{self.bil1}{attr(0)} - {fg(4)}{self.bil2}{attr(0)} = {fg(2)}{attr(1)}{self.bil1 - self.bil2}{attr(0)}")
  
  def kali(self):
    print(f"    Hasil : {fg(4)}{self.bil1}{attr(0)} * {fg(4)}{self.bil2}{attr(0)} = {fg(2)}{attr(1)}{self.bil1 * self.bil2}{attr(0)}")
  
  def bagi(self):
    print(f"    Hasil : {fg(4)}{self.bil1}{attr(0)} / {fg(4)}{self.bil2}{attr(0)} = {fg(2)}{attr(1)}{self.bil1 / self.bil2:.2f}{attr(0)}")
  
  def mod(self):
    print(f"    Hasil : {fg(4)}{self.bil1}{attr(0)} % {fg(4)}{self.bil2}{attr(0)} = {fg(2)}{attr(1)}{self.bil1 % self.bil2:.2f}{attr(0)}")

while(True):
  header()
  try:
    bil1 = int(input(f"    Masukkan bilangan 1        : {fg(4)}{attr(1)}"))
  except:
    clear()
    print(f"    {attr(0)}{bg(1)}Input tidak valid! Masukkan nilai integer{attr(0)}")
    continue
  
  op = input(f"\n{attr(0)}    Pilih operator (+,-,*,/,%) : {fg(4)}{attr(1)}")
  if not op in ('+','-','*','/','%'):
    clear()
    print(f"    {attr(0)}{bg(1)}Input tidak valid! Pilih operator yang benar{attr(0)}")
    continue
  
  try:
    bil2 = int(input(f"\n{attr(0)}    Masukkan bilangan 2        : {fg(4)}{attr(1)}"))
    print(attr(0))
    break
  except:
    clear()
    print(f"    {attr(0)}{bg(1)}Input tidak valid! Masukkan nilai integer{attr(0)}")
    continue
  
calc = Kalkulator(bil1,bil2)

clear()
header()
if op == '+':
  calc.tambah()
elif op == '-':
  calc.kurang()
elif op == '*':
  calc.kali()
elif op == '/':
  calc.bagi()
elif op == '%':
  calc.mod()