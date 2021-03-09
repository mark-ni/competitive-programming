import java.util.*;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Main {
  int b, l, d;
  int[] bookScores = new int[b];

  public static void main(String[] args) throws Exception {
    // INPUT PHASE
    Scanner scan = new Scanner(new File("a_example.txt"));
    //BufferedReader f = new BufferedReader(new FileReader("a_example.txt"));
    //PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("a_example_out.txt")));
    b = scan.nextInt();
    l = scan.nextInt();
    d = scan.nextInt();
    Library[] libraries = new Library[l];
    for (int i = 0; i < b; i++) {
      bookScores[i] = scan.nextInt();
    }
    for (int i = 0; i < l; i++) {
      int nb = scan.nextInt();
      int sd = scan.nextInt();
      int nbsd = scan.nextInt();
      int[][] bookids = new int[2][nb];
      for(int i = 0; i < nb; i++) {
        bookids[0][i] = scan.nextInt();
        bookids[1][i] = bookScores[i];
      }
      libraries[i] = new Library(bookids, nb, sd, nbsd, i);
    }

    //CHOOSING LIBRARIES
    ArrayList<Library> chosenLibraries = new ArrayList<Library>();
    Collections.sort(libraries);
    int totalSignUpDays = 0;
    int currIndex = 0;
    while (true) {
      totalSignUpDays += libraries[currIndex].signUpDays;
      if (totalSignUpDays >= d) {
        break;
      }
      chosenLibraries.add(libraries[currIndex]);
      currIndex++;
    }

    //OUTPUT
    Collections.sort(chosenLibraries, new SortTopHeavy());
    System.out.println(chosenLibraries.size());
    int currDay;
    for (int i = 0; i < chosenLibraries.size(); i++) {
      foo(chosenLibraries.get(i));
    }
  }
}
/*#Pseudocode:
#sorting the libraries from the least signup days to most and choosing a subset of libraries from that = L (maybe not just least signup days, maybe make an algorithm including the sum of the elements, and the number of books per day)
#from L, sorting the libraries from most bottom heavy to most top heavy with some kind of madeup algorithm*/