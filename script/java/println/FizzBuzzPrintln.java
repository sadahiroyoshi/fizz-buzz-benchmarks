public class FizzBuzzPrintln {
    public static void main(String[] args) { 
        int n = Integer.parseInt(args[0]); // messy code

        // long startTime = System.currentTimeMillis();
        // IntStream.rangeClosed(1, n) is slower than simple for loop 
        for (int i=1; i<=n; i++) {
            if (i%3==0 && i%5==0) {
                // System.out.print("fizzbuzz\n"); is almost same as println.
                System.out.println("fizzbuzz");
            } else if (i%3==0) {
                System.out.println("fizz");
            } else if (i%5==0) {
                System.out.println("buzz");
            } else {
                System.out.println(i);
            }
        }
        // long endTime = System.currentTimeMillis();
        // System.out.println("elapsed_time:" + ((endTime - startTime)/1000.00) + "[sec]");
    }
}
