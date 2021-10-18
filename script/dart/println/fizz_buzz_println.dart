// import 'dart:async';

main(List<String> args) {
    int n = int.parse(args[0]);
    // Stopwatch s = Stopwatch();

    // s.start();
    for (var i = 1; i <= n; i++) {
        if (i % 15 == 0) {
            print("fizzbuzz");
        } else if (i % 3 == 0) {
            print("fizz");
        } else if (i % 5 == 0) {
            print("buzz");
        } else {
            print(i);
        }
    }
    // var time = s.elapsed;
    // print("elapsed_time:${time.inMilliseconds/1000}[sec]");
}
