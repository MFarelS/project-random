#include <iostream>
#include <stdlib.h>
using namespace std;

int main(){
  string nama, prodi, nim;
  
  printf("===== PROGRAM DATA MAHASISWA =====\n");
  cout << "Masukkan nama  : "; 
  getline(std::cin, nama);
  cout << "Masukkan NIM   : "; 
  getline(std::cin, nim);
  cout << "Masukkan prodi : "; 
  getline(std::cin, prodi);
  system("clear");
  
  printf("\n\n===== PROGRAM DATA MAHASISWA =====\n");
  cout << "Nama  : " << nama;
  cout << "\nNIM   : " << nim;
  cout << "\nProdi : " << prodi;
}