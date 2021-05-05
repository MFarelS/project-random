class tes_perulangan{
  public static void main(String [] args){
    for(int i = 1; i <= 1000; i++){
      String separator = (i == 1000) ? " " : ", ";
      System.out.print(i + separator);
    }
  }
}