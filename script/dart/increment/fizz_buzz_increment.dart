// import 'dart:async';

main(List<String> args) {
    int n = int.parse(args[0]);
    // Stopwatch s = Stopwatch();

    int fizzbuzz = 0;
    int fizz = 0;
    int buzz = 0;
    int none = 0;

    // s.start();
    for (var i = 1; i <= n; i++) {
        if (i % 15 == 0) {
            fizzbuzz++;
        } else if (i % 3 == 0) {
            fizz++;
        } else if (i % 5 == 0) {
            buzz++;
        } else {
            none++;
        }
    }
    // var time = s.elapsed;
    // print('elapsed_time:${time.inMilliseconds/1000}[sec]');
    print("fizzbuzz:$fizzbuzz");
    print("fizz:$fizz");
    print("buzz:$buzz");
    print("none:$none");
}
