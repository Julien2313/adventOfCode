extern crate time;

use std::io::Error;
use std::fs;

mod aoc2018;

fn main()  {
    let input = read("src/aoc2018/day1/input.txt".to_string()).expect("error from read");
    let now = time::now();
    println!("{}", aoc2018::day1::main::p1(&input));
    println!("{}", aoc2018::day1::main::p2(&input));
    println!("{}", time::now() - now)
}

fn read(path: String) -> Result<String, Error> {
    let input = fs::read_to_string(path)?;
    return Ok(input);
}