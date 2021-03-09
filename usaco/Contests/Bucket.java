public class Bucket {
  private int max;
  private int curr;

  public Bucket(int max, int curr) {
    this.max = max;
    this.curr = curr;
  }

  public int getCurr() {
    return curr;
  }

  public int getMax() {
    return max;
  }

  public void setCurr(int curr) {
    this.curr = curr;
  }

  public String toString() {
    return "" + curr;
  }

  public void pour(Bucket b) {
    if (b.getCurr() + curr > b.getMax()) {
      curr -= (b.getMax() - b.getCurr());
      b.setCurr(b.getMax());
    }
    else {
      b.setCurr(b.getCurr() + curr);
      curr = 0;
    }
  }
}