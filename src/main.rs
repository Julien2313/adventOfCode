use std::time;

mod aoc2022;

fn main() {
    let now = time::Instant::now();
    println!("{}", aoc2022::day3::main::p1());
    println!("{}", aoc2022::day3::main::p2());

    println!("time : {}µs", now.elapsed().as_micros());
}
