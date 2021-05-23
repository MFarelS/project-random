//deklarasi preprocessor
#include <iostream>
#include <stdlib.h>
using namespace std;

// prosedur cleanscreen
void clear() {
  system("clear");
}

//kelas mahasiswa
class Mahasiswa {
  //properti mahasiswa
  private:
    string nama,fakultas,prodi,nim;

  //method mahasiswa
  public:
    void setNama(string nama) {
      this->nama = nama;
    }

    string getNama() {
      return nama;
    }
  
    void setNim(string nim) {
      this->nim = nim;
    }
  
    string getNim() {
      return nim;
    }

    void setFakultas(string fakultas) {
      this->fakultas = fakultas;
    }
  
    string getFakultas() {
      return fakultas;
    }
  
    void setProdi(string prodi) {
      this->prodi = prodi;
    }
  
    string getProdi() {
      return prodi;
    }
    
    bool check_number(string str) {
      for (int i = 0; i < str.length(); i++)
        if (isdigit(str[i]) == false)
          return false;
          return true;
    }

    void inputNama() {
      cout << "Siapa nama anda? ";
      getline(cin, nama);
      if(!check_number(nama)){
        setNama(nama); clear();
      }else{
        clear();
        cout << "Input tidak valid. Masukkan nama yang benar!" << endl;
        inputNama();
      }
    }
  
    void inputNim() {
      cout << "Selamat datang, " << getNama() << endl << endl;
      cout << "Berapa NIM anda? ";
      cin >> nim;
      if(check_number(nim)){
        setNim(nim); clear();
      }else{
        clear();
        cout << "Input tidak valid. Masukkan NIM dengan benar!" << endl;
        inputNim();
      }
    }

    void inputFakultas() {
      int pilihan,pilihan2;
      cout << "Apa Fakultas Anda?" << endl;
      cout << "1. Fakultas Pertanian" << endl;
      cout << "2. Fakultas Keguruan dan Ilmu Pendidikan" << endl;
      cout << "3. Fakultas Teknologi Informasi" << endl;
      cout << "4. Fakultas Ekonomi" << endl;
      cout << "5. Fakultas Ilmu Sosial dan Politik" << endl;
      cout << "6. Fakultas Matematika dan Ilmu Pengetahuan Alam" << endl;
      cout << "7. Fakultas Ilmu Kesehatan" << endl << endl;
      cout << "Pilih nomor: ";
      cin >> pilihan;
      if(check_number(pilihan)){
        switch(pilihan) {
          case 1:
            fakultas = "Fakultas Pertanian";
            clear();
            cout << "Apa Prodi Anda?" << endl;
            cout << "1. Agroteknologi" << endl;
            cout << "2. Agribisnis" << endl << endl;
            cout << "Pilih nomor: ";
            cin >> pilihan2;
            if(check_number(pilihan2)){
              switch(pilihan2) {
                case 1: prodi = "Agroteknologi"; break;
                case 2: prodi = "Agribisnis"; break;
                default: 
                  clear();
                  cout << "Pilihan tidak valid. Masukkan pilihan dengan benar!" << endl;
                  inputFakultas();
                  break;
              }
            }else{
              clear();
              cout << "Input tidak valid. Masukkan nama yang benar!" << endl;
              inputFakultas();
            }
            break;
          case 2:
            fakultas = "Fakultas Keguruan dan Ilmu Pendidikan";
            clear();
            cout << "Apa Prodi Anda?" << endl;
            cout << "1. Pendidikan Geografi" << endl;
            cout << "2. Pendidikan Bahasa dan Sastra Indonesia" << endl;
            cout << "3. Pendidikan Bahasa Inggris" << endl;
            cout << "4. Pendidikan IPS" << endl << endl;
            cout << "Pilih nomor: ";
            cin >> pilihan2;
            if(check_number(pilihan2)){
              switch(pilihan2) {
                case 1: prodi = "Pendidikan Geografi"; break;
                case 2: prodi = "Pendidikan Bahasa dan Sastra Indonesia"; break;
                case 3: prodi = "Pendidikan Bahasa Inggris"; break;
                case 4: prodi = "Pendidikan IPS"; break;
                default: 
                  clear();
                  cout << "Pilihan tidak valid. Masukkan pilihan dengan benar!" << endl;
                  inputFakultas();
                  break;
              }
            }else{
              clear();
              cout << "Input tidak valid. Masukkan nama yang benar!" << endl;
              inputFakultas();
            }
            break;
          case 3:
            fakultas = "Fakultas Teknologi Informasi";
            clear();
            cout << "Apa Prodi Anda?" << endl;
            cout << "1. Teknik Informatika" << endl;
            cout << "2. Sistem Informasi" << endl << endl;
            cout << "Pilih nomor: ";
            cin >> pilihan2;
            if(check_number(pilihan2)){
              switch(pilihan2) {
                case 1: prodi = "Teknik Informatika"; break;
                case 2: prodi = "Sistem Informasi"; break;
                default:
                  clear();
                  cout << "Pilihan tidak valid. Masukkan pilihan dengan benar!" << endl;
                  inputFakultas();
                  break;
              }
            }else{
              clear();
              cout << "Input tidak valid. Masukkan nama yang benar!" << endl;
              inputFakultas();
            }
            break;
          case 4:
            fakultas = "Fakultas Ekonomi";
            prodi = "Akuntansi";
            break;
          case 5:
            fakultas = "Fakultas Ilmu Sosial dan Politik";
            prodi = "Ilmu Pemerintahan";
            break;
          case 6:
            fakultas = "Fakultas Matematika dan Ilmu Pengetahuan Alam";
            prodi = "Matematika";
            break;
          case 7:
            fakultas = "Fakultas Ilmu Kesehatan";
            prodi = "Ilmu Keperawatan";
            break;
          default: 
            clear();
            cout << "Pilihan tidak valid. Masukkan pilihan dengan benar!" << endl;
            inputFakultas();
            break;
        }
      }else{
        clear();
        cout << "Input tidak valid. Masukkan nama yang benar!" << endl;
        inputFakultas();
      }
      setFakultas(fakultas); setProdi(prodi);
      clear();
    }
    
    void tampilData(){
      cout << "Data Mahasiwa UNIBBA\n";
      cout << "Nama     : " << getNama() << endl;
      cout << "NIM      : " << getNim() << endl;
      cout << "Fakultas : " << getFakultas() << endl;
      cout << "Prodi    : " << getProdi() << endl;
    }
};

//fungsi utama
int main() {
  //instansiasi objek
  Mahasiswa obj;

  //memanggil method objek
  obj.inputNama();
  obj.inputNim();
  obj.inputFakultas();
  obj.tampilData();

  return 0;
}
