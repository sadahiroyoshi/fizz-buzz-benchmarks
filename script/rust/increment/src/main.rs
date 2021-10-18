use std::env;
// use std::time::Instant;

fn main() {
    let args: Vec<String> = env::args().collect();
    let n: i32 = args[1].parse().unwrap(); // messy code

    let mut fizzbuzz = 0;
    let mut fizz = 0;
    let mut buzz = 0;
    let mut none = 0;

    // let start = Instant::now();
    for i in 1..=n {
        if i % 15 == 0 {
            fizzbuzz += 1;
        } else if i % 3 == 0 {
            fizz += 1;
        } else if i % 5 == 0 {
            buzz += 1;
        } else {
            none += 1;
        }
        // match is slower than simple for loop
        // match n % 15 {
        //     0 => fizzbuzz += 1,
        //     5 | 10 => buzz += 1,
        //     3 | 6 | 9 | 12 => fizz += 1,
        //     _ => none += 1,
        // }
    }
    // let end = start.elapsed();
    // println!("elapsed_time:{}.{:03}[sec]", end.as_secs(), end.subsec_nanos() / 1_000_000);
    print!("fizzbuzz:{}\n", fizzbuzz);
    print!("fizz:{}\n", fizz);
    print!("buzz:{}\n", buzz);
    print!("none:{}\n", none);
}
