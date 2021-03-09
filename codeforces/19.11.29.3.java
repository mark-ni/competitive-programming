import java.util.Scanner;

public class Main
{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int m = scan.nextInt();
		for (int i = 0; i < m; i++) {
		    getAns(scan.nextInt());
		}
	}
	
	public static void getAns(int n) {
		//try again
	    int k = (int) (Math.sqrt(n));
	    
	    int asdf = k;
	    int total = k;
	    if (asdf == n/asdf) {
	        asdf -= 1;
	    }
	    total += asdf + 1;
        System.out.println(total);

	    
	    System.out.print("0");
	    
	    for (int i = 1; i < k + 1; i++) {
	        System.out.print(" " + i);
	    }
	    
	    if (k == n/k) {
	        k -= 1;
	    }
	    
	    for (int j = k; j > 0; j--) {
	        System.out.print(" " + n/j);
	    }
	    
	    System.out.println();
	}
}