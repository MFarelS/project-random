#include <iostream>
#include <stdlib.h>
using namespace std;

// prosedur cleanscreen
void clear(){
	system("clear");
}

//kelas mahasiswa
class Mahasiswa{
	private:
		string nama, fakultas, prodi;
		int nim;
		
	public:
		void setNama(string nama){
			this->nama = nama;
		}	

		string getNama(){
			return nama;
		}

		void setNim(int nim){
			this->nim = nim;
		}	

		int getNim(){
			return nim;
		}

		void setFakultas(string fakultas){
			this->fakultas = fakultas;
		}	

		string getFakultas(){
			return fakultas;
		}

		void setProdi(string prodi){
			this->prodi = prodi;
		}	

		string getProdi(){
			return prodi;
		}
};

//fungsi utama
int main(){
	string nama, fakultas, prodi;
	int nim, pilihan, pilihan2;
	Mahasiswa obj;

	cout << "Siapa nama anda? "; 
	getline(cin, nama);
	obj.setNama(nama); clear();
	
	cout << "Selamat datang, " << obj.getNama() << endl << endl;
	cout << "Berapa NIM anda? ";
	cin >> nim;
	obj.setNim(nim); clear();

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

	switch(pilihan){
		case 1: 
			fakultas = "Fakultas Pertanian";
			clear();
			cout << "Apa Prodi Anda?" << endl;
			cout << "1. Agroteknologi" << endl;
			cout << "2. Agribisnis" << endl << endl;
			cout << "Pilih nomor: ";
			cin >> pilihan2;
			switch(pilihan2){
				case 1: prodi = "Agroteknologi"; break;
			  case 2: prodi = "Agribisnis"; break;
				default: cout << "Pilihan tidak valid!"; return 0;
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
			switch(pilihan2){
				case 1: prodi = "Pendidikan Geografi"; break;
			  case 2: prodi = "Pendidikan Bahasa dan Sastra Indonesia"; break;
			  case 3: prodi = "Pendidikan Bahasa Inggris"; break;
			  case 4: prodi = "Pendidikan IPS"; break;
				default: cout << "Pilihan tidak valid!"; return 0;
			}
			break; 
		case 3: 
			fakultas = "Fakultas Teknologi Informasi"; 
			clear();
			cout << "Apa Prodi Anda?" << endl;
			cout << "1. Teknik Informatika" << endl;
			cout << "2. Sistem Informasi" << endl << endl	;
			cout << "Pilih nomor: ";
			cin >> pilihan2;
			switch(pilihan2){
				case 1: prodi = "Teknik Informatika"; break;
			  case 2: prodi = "Sistem Informasi"; break;
				default: cout << "Pilihan tidak valid!"; return 0;
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
		default: cout << "Pilihan tidak valid!"; return 0; 
	}	
	obj.setFakultas(fakultas); obj.setProdi(prodi);
	clear();

	cout << "Data Mahasiwa UNIBBA\n";
	cout << "Nama     : " << obj.getNama() << endl;
	cout << "NIM      : " << obj.getNim() << endl;
	cout << "Fakultas : " << obj.getFakultas() << endl;
	cout << "Prodi    : " << obj.getProdi() << endl;

	return 0;
}
