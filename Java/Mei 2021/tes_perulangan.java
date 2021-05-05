class tes_perulangan{
  public static void main(String [] args){
    for(int i = 1; i <= 10; i++){
      String separator = (i != 10) ? ", " : "";
      System.out.printf("Hello world %d" + separator + "\n", i);
    }
  }
}