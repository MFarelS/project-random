//impor library java
import java.util.Scanner;

//kelas mahasiswa
class dataMahasiswa {
  //variabel input
  static Scanner in = new Scanner(System.in);
  //properti mahasiswa
  private String nama, fakultas, prodi;
  private int nim;

  //method mahasiswa
  public static void clear() {
    System.out.print("\033[H\033[2J");
    System.out.flush();
  }
  void setNama(String nama) {
    this.nama = nama;
  }

  String getNama() {
    return this.nama;
  }

  void setNim(int nim) {
    this.nim = nim;
  }

  int getNim() {
    return this.nim;
  }

  void setFakultas(String fakultas) {
    this.fakultas = fakultas;
  }

  String getFakultas() {
    return this.fakultas;
  }

  void setProdi(String prodi) {
    this.prodi = prodi;
  }

  String getProdi() {
    return this.prodi;
  }

  void inputNama() {
    System.out.print("Siapa nama anda? ");
    String nama = in .nextLine();
    setNama(nama);
    clear();
  }

  void inputNim() {
    do {
      try {
        System.out.println("Selamat datang, " + getNama() + "\n");
        System.out.print("Berapa NIM anda? ");
        nim = in .nextInt();
        setNim(nim);
        clear();
        break;
      } catch (Exception ex) {
        clear();
        System.out.println("Input tidak valid. Masukkan NIM dengan benar!");
      } in .nextLine();
    } while (true);
  }

  void inputFakultas() {
    int pilihan, pilihan2;
    boolean valid = false;
    do {
      try {
        System.out.print(
          "Apa Fakultas Anda?\n" +
          "1. Fakultas Pertanian\n" +
          "2. Fakultas Keguruan dan Ilmu Pendidikan\n" +
          "3. Fakultas Teknologi Informasi\n" +
          "4. Fakultas Ekonomi\n" +
          "5. Fakultas Ilmu Sosial dan Politik\n" +
          "6. Fakultas Matematika dan Ilmu Pengetahuan Alam\n" +
          "7. Fakultas Ilmu Kesehatan\n\n" +
          "Pilih nomor: ");

        pilihan = in .nextInt();
        switch (pilihan) {
        case 1:
          fakultas = "Fakultas Pertanian";
          clear();
          System.out.print(
            "Apa Prodi Anda?\n" +
            "1. Agroteknologi\n" +
            "2. Agribisnis\n\n" +
            "Pilih nomor: ");
          pilihan2 = in .nextInt();
          switch (pilihan2) {
          case 1:
            prodi = "Agroteknologi";
            valid = true;
            break;
          case 2:
            prodi = "Agribisnis";
            valid = true;
            break;
          default:
            clear();
            System.out.println("Pilihan tidak valid. Masukkan pilihan dengan benar!");
            inputFakultas();
            break;
          }
          break;
        case 2:
          fakultas = "Fakultas Keguruan dan Ilmu Pendidikan";
          clear();
          System.out.print(
            "Apa Prodi Anda?\n" +
            "1. Pendidikan Geografi\n" +
            "2. Pendidikan Bahasa dan Sastra Indonesia\n" +
            "3. Pendidikan Bahasa Inggris\n" +
            "4. Pendidikan IPS\n\n" +
            "Pilih nomor: ");
          pilihan2 = in .nextInt();
          switch (pilihan2) {
          case 1:
            prodi = "Pendidikan Geografi";
            valid = true;
            break;
          case 2:
            prodi = "Pendidikan Bahasa dan Sastra Indonesia";
            valid = true;
            break;
          case 3:
            prodi = "Pendidikan Bahasa Inggris";
            valid = true;
            break;
          case 4:
            prodi = "Pendidikan IPS";
            valid = true;
            break;
          default:
            clear();
            System.out.println("Pilihan tidak valid. Masukkan pilihan dengan benar!");
            inputFakultas();
            break;
          }
          break;
        case 3:
          fakultas = "Fakultas Teknologi Informasi";
          clear();
          System.out.print(
            "Apa Prodi Anda?\n" +
            "1. Teknik Informatika\n" +
            "2. Sistem Informasi\n\n" +
            "Pilih nomor: ");
          pilihan2 = in .nextInt();
          switch (pilihan2) {
          case 1:
            prodi = "Teknik Informatika";
            valid = true;
            break;
          case 2:
            prodi = "Sistem Informasi";
            valid = true;
            break;
          default:
            clear();
            System.out.println("Pilihan tidak valid. Masukkan pilihan dengan benar!");
            inputFakultas();
            break;
          }
          break;
        case 4:
          fakultas = "Fakultas Ekonomi";
          prodi = "Akuntansi";
          valid = true;
          break;
        case 5:
          fakultas = "Fakultas Ilmu Sosial dan Politik";
          prodi = "Ilmu Pemerintahan";
          valid = true;
          break;
        case 6:
          fakultas = "Fakultas Matematika dan Ilmu Pengetahuan Alam";
          prodi = "Matematika";
          valid = true;
          break;
        case 7:
          fakultas = "Fakultas Ilmu Kesehatan";
          prodi = "Ilmu Keperawatan";
          valid = true;
          break;
        default:
          clear();
          System.out.println("Pilihan tidak valid. Masukkan pilihan dengan benar!");
          inputFakultas();
          break;
        }
        break;
      } catch (Exception ex) {
        clear();
        System.out.println("Pilihan tidak valid. Masukkan pilihan dengan benar!");
      } in .nextLine();
    } while (valid == false);
    setFakultas(fakultas);
    setProdi(prodi);
  }

  void tampilData() {
    clear();
    System.out.print(
      "                 Data Mahasiswa UNIBBA\n" +
      "======================================================="+
      "\nNama     : " + getNama() +
      "\nNIM      : " + getNim() +
      "\nFakultas : " + getFakultas() +
      "\nProdi    : " + getProdi()+
      "\n=======================================================");
  }

  //fungsi utama
  public static void main(String[] args) {
    //instansiasi objek
    dataMahasiswa obj = new dataMahasiswa();

    //memanggil method objek
    obj.inputNama();
    obj.inputNim();
    obj.inputFakultas();
    obj.tampilData(); in .close();
  }
}