use std::env;
// use std::time::Instant;

fn main() {
    let args: Vec<String> = env::args().collect();
    let n: i32 = args[1].parse().unwrap(); // messy code

    // let start = Instant::now();
    for i in 1..=n {
        if i % 15 == 0 {
            print!("{}\n", "fizzbuzz");
        } else if i % 3 == 0 {
            print!("{}\n", "fizz");
        } else if i % 5 == 0 {
            print!("{}\n", "buzz");
        } else {
            print!("{}\n", i);
        }
    }
    // let end = start.elapsed();
    // println!("elapsed_time:{}.{:03}[sec]", end.as_secs(), end.subsec_nanos() / 1_000_000);
}
