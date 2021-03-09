import java.util.*;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;
import java.io.PrintWriter;

public class Main {

  public static void main(String[] args) throws Exception {
    // INPUT PHASE
    Scanner scan = new Scanner(new File("f_libraries_of_the_world.txt"));
    //BufferedReader f = new BufferedReader(new FileReader("a_example.txt"));
    //PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("a_example_out.txt")));

    // PrintWriter out = new PrintWriter(new File("out_f.txt"));

    int b, l, d;

    b = scan.nextInt();
    l = scan.nextInt();
    d = scan.nextInt();
    int[] bookScores = new int[b];
    Library[] libraries = new Library[l];

    for (int i = 0; i < b; i++) {
      bookScores[i] = scan.nextInt();
    }

    for (int i = 0; i < l; i++) {
      int nb = scan.nextInt();
      int sd = scan.nextInt();
      int nbsd = scan.nextInt();
      int[][] bookids = new int[2][nb];
      for(int j = 0; j < nb; j++) {
        bookids[0][j] = scan.nextInt();
        bookids[1][j] = bookScores[j];
      }
      libraries[i] = new Library(bookids, nb, sd, nbsd, i);
    }


////////////////////////////////////////////////////////////////

    // Mark stuff
    ArrayList<Library> chosenLibraries = new ArrayList<Library>();
    Arrays.sort(libraries);
    int totalSignUpDays = 0;
    int currIndex = 0;
    while (currIndex < libraries.length) {
      totalSignUpDays += libraries[currIndex].signUpDays;
      if (totalSignUpDays >= d) {
        break;
      }
      chosenLibraries.add(libraries[currIndex]);
      currIndex++;
    }


    //OUTPUT
    out.println(chosenLibraries.size());
    for (Library lib : chosenLibraries) {
      int numbooksoutput = Math.min((d - lib.signUpDays) * lib.nbpd, lib.numBooks);
      out.println(lib.libID + " " + numbooksoutput);

      lib.sorta();
      
      for (int j = 1; j <= numbooksoutput; j++)
        out.print(lib.sortedBookIDs[lib.sortedBookIDs.length - j] + " ");
      out.println();
    }

  }
  


//-------------------------------------------------------
  private static class Library implements Comparable<Library> {
    public int libID;
    public int numBooks;
    public int[][] bookIDs;
    public int signUpDays;
    public int nbpd;
    public int[] sortedBookIDs;

    public void sorta() {
      for (int i = 0; i < bookIDs.length-1; i++) {
        int min = i;
        for (int j = i + 1; j < bookIDs.length; j++) {
          if (bookIDs[1][j] < bookIDs[1][min]) {
            min = j;
          }
        }
        int temp = bookIDs[1][min];
        bookIDs[1][min] = bookIDs[1][i];
        bookIDs[1][i] = temp;
        int temp1 = bookIDs[0][min];
        bookIDs[0][min] = bookIDs[1][i];
        bookIDs[0][i] = temp1;
      }
      sortedBookIDs = bookIDs[0];
    }

    public Library(int[][] bookIDs, int numBooks, int signUpDays, int nbpd, int libID) {
      this.bookIDs = bookIDs;
      this.numBooks = numBooks;
      this.signUpDays = signUpDays;
      this.nbpd = nbpd;
      this.libID = libID;
    }

    public int compareTo(Library other) {
      if (signUpDays < other.signUpDays) {
        return -100;
      } else if (signUpDays > other.signUpDays) {
        return 100;
      } else { 
        return 0;
      }
    }

    public int getTopHeavyScore() {
      ArrayList<Integer> bookIDsCopy = new ArrayList<>(numBooks);
      for (int i = 0; i < numBooks; i++) {
        bookIDsCopy.add(bookIDs[i][1]);
      }
      Collections.sort(bookIDsCopy, Collections.reverseOrder());

      return (int) ((median(bookIDsCopy) - mean(bookIDsCopy)) / (median(bookIDsCopy)));
    }

    private double mean(ArrayList<Integer> m) {
      int sum = 0;
      for (int i = 0; i < m.size(); i++) {
        sum += m.get(i);
      }
      return sum / ((double) m.size());
    }
    private double median(ArrayList<Integer> m) {
      int middle = m.size()/2;
      if (m.size()%2 == 1) {
        return (double) m.get(middle);
      } else {
        return ((double) m.get(middle-1) + m.get(middle)) / 2.0;
      }
    }
  }


  private class SortTopHeavy implements Comparator<Library> {
    public int compare(Library a, Library b) {
      int topHeavyA = a.getTopHeavyScore();
      int topHeavyB = b.getTopHeavyScore();
      if (topHeavyA > topHeavyB) {
        return 1;
      } else if (topHeavyA < topHeavyB) {
        return -1;
      }
      return 0;
    }
  }
}
/*#Pseudocode:
#sorting the libraries from the least signup days to most and choosing a subset of libraries from that = L (maybe not just least signup days, maybe make an algorithm including the sum of the elements, and the number of books per day)
#from L, sorting the libraries from most bottom heavy to most top heavy with some kind of madeup algorithm*/