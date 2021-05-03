#include <iostream>
#include <math.h>
using namespace std;

int tambah(int a, int b) {
  return a + b;
}

int kurang(int x, int y) {
  return x - y;
}

int kali(int p, int q) {
  return p * q;
}

int bagi(int c, int d) {
  return c / d;
}

int mod(int e, int f) {
  return e % f;
}

int pangkat(int g, int h) {
  return pow(g, h);
}

int main() {
  printf("Hasil penjumlahan dari 2 + 2 = %i", tambah(2, 2));
  printf("Hasil pengurangan dari 3 - 4 = %i", kurang(3, 4));
  printf("Hasil perkalian dari   6 * 2 = %i", kali(6, 2));
  printf("Hasil pembagian dari   8 / 4 = %i", bagi(8, 4));
  printf("Hasil modulus dari     7 % 3 = %d", mod(7, 3));
  printf("Hasil pangkat dari    5 ** 4 = %i", pangkat(5, 4));
}
