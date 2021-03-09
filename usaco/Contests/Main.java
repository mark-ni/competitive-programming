/*
ID: your_id_here
LANG: JAVA
TASK: test
*/
import java.io.*;
import java.util.*;

class Main {
  public static void main (String [] args) throws IOException {
    // Use BufferedReader rather than RandomAccessFile; it's much faster
    BufferedReader f = new BufferedReader(new FileReader("mixmilk.in"));
    PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("mixmilk.out")));
    // Use StringTokenizer vs. readLine/split -- lots faster
    StringTokenizer st = new StringTokenizer(f.readLine());
						  // Get line, break into tokens
    int i1 = Integer.parseInt(st.nextToken());    // first integer
    int i2 = Integer.parseInt(st.nextToken());    // second integer
    out.println(solve());                           // output result
    out.close();                                  // close the output file
    System.exit(0);                               // don't omit this!
  }

  public static void solve() {}
    String inp = ""

    int aMax = 10;
    int aCurr = 3;
    int bMax = 11;
    int bCurr = 4;
    int cMax = 12;
    int cCurr = 5;
    int[][] listOfValues = {{aMax, aCurr},{bMax,bCurr},{cMax,cCurr}};

    Bucket[] bucketList = new Bucket[3];
    for (int i = 0; i < 3; i++) {
      bucketList[i] = new Bucket(listOfValues[i][0], listOfValues[i][1]);
      System.out.println(bucketList[i]);
    }

    int currentIndex = 0;
    for (int counter = 0; counter < 99; counter++) {
      int nextIndex = (currentIndex + 1) % 3;
      bucketList[currentIndex].pour(bucketList[nextIndex]);
      currentIndex = nextIndex;
      //System.out.println(bucketList[0].getCurr() + ", " + bucketList[1].getCurr() + ", " + bucketList[2].getCurr());
      if (checkLoop(bucketList)) {
        counter = 96 + currentIndex;
      }
    }
    for (Bucket buck:bucketList) {
      System.out.println(buck);
    }
  }

  public static boolean checkLoop(Bucket[] asdf) {
    if (asdf[0].getCurr() == 0) {
      if (asdf[1].getCurr() == 0 || asdf[2].getCurr() == 0){
        return true;
      }
    }
    else if (asdf[1].getCurr() == 0 && asdf[2].getCurr() == 0) {
      return true;
    }

    return false;
  }
}