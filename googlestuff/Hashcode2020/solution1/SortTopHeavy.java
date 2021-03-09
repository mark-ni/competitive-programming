public class SortTopHeavy implements Comparator<Library> {
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