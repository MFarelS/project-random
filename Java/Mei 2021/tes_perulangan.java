class tes_perulangan{
  public static void main(String [] args){
    for(int i = 1; i <= 100; i++){
      String separator = (i != 100) ? ", " : "";
      System.out.printf(i + separator);
    }
  }
}
