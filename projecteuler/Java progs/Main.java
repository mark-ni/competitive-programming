package aaa;

class Main {

  private String[] colors = ["B","W"];

  public static void main(String[] args) {
    int dimensions = 1001;
    int stopIndex = (dimensions-1)/2;

    int[] ULlist;
 
    int ULsum = pathFormula(4, 2, stopIndex);
    int DRsum = pathFormula(4, -2, stopIndex);
    int DLsum = pathFormula(4, 0, stopIndex);
    int URsum = pathFormula(4, 4, stopIndex);
 
    System.out.println(ULsum + URsum + DLsum + DRsum - 3);
  }
 
  public static int sumList(int[] arrayyy) {
    int sum = 0;
    for (int x:arrayyy) {
      sum += x;
    }
    return sum;
  }
 
  public static int pathFormula(int m, int b, int stopIndex) {
    int rL;
    int[] listOfNums = new int[stopIndex+1];
    listOfNums[0] = 1;
    for (int i = 0; i < stopIndex; i++) {
      rL = 2*i + 1;
      listOfNums[i+1] = listOfNums[i] + m * rL + b;
    }
    int sum = sumList(listOfNums);
    return sum;
  }
}