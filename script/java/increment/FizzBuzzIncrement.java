public class FizzBuzzIncrement {
    public static void main(String[] args) { 
        int n = Integer.parseInt(args[0]); // messy code

        int fizzbuzz = 0;
        int fizz = 0;
        int buzz = 0;
        int none = 0;

        // long startTime = System.currentTimeMillis();
        // IntStream.rangeClosed(1, n) is slower than simple for loop 
        for (int i=1; i<=n; i++) {
            if (i%3==0 && i%5==0) {
                fizzbuzz++;
            } else if (i%3==0) {
                fizz++;
            } else if (i%5==0) {
                buzz++;
            } else {
                none++;
            }
        }

        // long endTime = System.currentTimeMillis();
        // System.out.println("elapsed_time:" + ((endTime - startTime)/1000.00) + "[sec]");
        System.out.println("fizzbuzz:" + fizzbuzz);
        System.out.println("fizz:" + fizz);
        System.out.println("buzz:" + buzz);
        System.out.println("none:" + none);
    }
}
