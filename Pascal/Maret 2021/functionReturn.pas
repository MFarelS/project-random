program functionReturn;
uses crt;

function tambah(a:integer; b:integer):integer;
  begin
    tambah := a + b;
  end;

function kurang(x:integer; y:integer):integer;
  begin
    kurang := x - y;
  end;

function kali(p:integer; q:integer):integer;
  begin
    kali := p * q;
  end;

function bagi(c:integer; d:integer):integer;
  begin
    bagi := c div d;
  end;

function modulus(e:integer; f:integer):integer;
  begin
    modulus := e mod f;
  end;

function pangkat(g:integer; h:integer):integer;
  var 
    i : integer; temp : integer;
  begin
    temp := 1;
    for i := 1 to h do
      begin
        temp := temp * g;
      end;
    pangkat := temp;
  end;

begin
  writeln('Hasil penjumlahan dari 2 + 2 = ', tambah(2, 2));
  writeln('Hasil pengurangan dari 3 - 4 = ', kurang(3, 4));
  writeln('Hasil perkalian dari   6 * 2 = ', kali(6, 2));
  writeln('Hasil pembagian dari   8 / 4 = ', bagi(8, 4));
  writeln('Hasil modulus dari     7 % 3 = ', modulus(7, 3));
  writeln('Hasil pangkat dari    5 ** 4 = ', pangkat(5, 4));
end.
