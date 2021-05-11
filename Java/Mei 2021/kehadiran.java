import java.util.Scanner;
class kehadiran{
  public static void main(String[] args){
    Scanner in = new Scanner(System.in);
    String output = "";
    int pilihan;
    System.out.print(
      "1 = Bisa hadir offline \n" +
      "2 = Jaringan bagus \n" +
      "3 = Tidak bisa hadir offline dan jaringan tidak bagus \n\n" +
      "Masukkan pilihan : "
    );
    pilihan = in.nextInt();
    switch(pilihan){
      case 1 : 
        output = "Sampai jumpa dikelas offline";
        break;
      case 2 : 
        output = "Silakan ikut kelas online";
        break;
      case 3 : 
        output = "Sampai jumpa tahun depan";
        break;
      default:
        output = "Pilihan tidak valid";
        break;
    }
    System.out.println("\n" + output);
    in.close();
  }
}