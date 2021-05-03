#include <iostream> 
#include <stdlib.h>
using namespace std;

int main() {
  int nomor;
  while (true) {
    cout << "Pilih Nomor! ";
    cin >> nomor;
    switch (nomor) {
      case 1:
        cout << "Satu\n";
        break;
      case 2:
        cout << "Dua\n";
        break;
      default:
        system("clear");
        cout << "Pilihan tidak valid!" << endl;
        continue;
    }
    break;
  }
  return 0;
}
