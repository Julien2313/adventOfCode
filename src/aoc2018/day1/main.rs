use std::collections::HashSet;
use std::cell::Cell;

pub fn p1(input: &String) {
    let mut freq:i32 = 0;

    for line in input.lines() {
        freq += line.parse::<i32>().unwrap();
    }
    println!("{}", freq);
}

pub fn p2(input: &String) {
    let mut freqs = HashSet::new();
    let freq = Cell::new(0);

    loop {
        for line in input.lines() {
            freq.set( freq.get() + line.parse::<i32>().unwrap());
            if freqs.contains(&freq.get()) {
                println!("{}", freq.get());
                return
            }
            freqs.insert(freq.get());
        } 
    }
}