public class Library implements Comparable<Library> {
  public int libID;
  public int numBooks;
  public int[] bookIDs;
  public int signUpDays;
  public int nbpd;
  public int[] sortedBookIDs;

  public Library(int[] bookIDs, int numBooks, int signUpDays, int nbpd, int libID) {
    this.bookIDs = bookIDs;
    this.numBooks = numBooks;
    this.signUpDays = signUpDays;
    this.nbpd = nbpd;
    this.libID = libID;
  }

  public void foo(int daysRemaining, int[] bookScores) {
    int[] bookIDsCopy = new int[numBooks];
    HashMap<Integer, Integer> reverseLookup = new HashMap<Integer, Integer>();
    for (int i = 0; i < numBooks; i++) {
      bookIDsCopy[i] = bookScores[bookIDs[i]];
      reverseLookup.put(bookIDsCopy[i], bookIDs[i]);
    }
    Arrays.sort(bookIDsCopy, Arrays.reverseOrder());
    System.out.print(libID + " ");

    int numBooksToShip = min(bookIDsCopy.length, (daysRemaining - signUpDays) * nbpd);
    
    System.out.println(numBooksToShip);

    for (int i = 0; i < numBookstoShip; i++ ) {
      System.out.print(reverseLookup.get(bookIDsCopy[i]) + " ");
    }
    System.out.println();
  }

  private int min(int a, int b) {
    if (a < b) {
      return a;
    }
    return b;
  }

  public int compareTo(Object other) {
    if (signUpDays < other.signUpDays) {
      return -100;
    } else if (signUpDays > other.signUpDays) {
      return 100;
    } else { 
      return 0;
    }
  }

  public int getTopHeavyScore() {
    int[] bookIDsCopy = new int[numBooks];
    for (int i = 0; i < numBooks; i++) {
      bookIDsCopy[i] = bookScores[bookIDs[i][1]];
    }
    Collections.sort(bookIDsCopy, Collections.reverseOrder());
    return (median(bookIDsCopy) - mean(bookIDsCopy)) /(median(bookIDsCopy));
  }

  private double mean(int[] m) {
    int sum = 0;
    for (int i = 0; i < m.length; i++) {
      sum += m[i];
    }
    return sum / ((double) m.length);
  }

  private double median(int[] m) {
    int middle = m.length/2;
    if (m.length%2 == 1) {
      return (double) m[middle];
    } else {
      return ((double) m[middle-1] + m[middle]) / 2.0;
    }
  }
}