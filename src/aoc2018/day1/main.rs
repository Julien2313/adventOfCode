use std::collections::HashSet;  

pub fn p1(input: &String) {
    let mut freq:i32 = 0;

    for line in input.lines() {
        freq += line.parse::<i32>().expect("Bad number");
    }
    println!("{}", freq);
}

pub fn p2(input: &String) {
    let mut freqs = HashSet::new();
    let mut freq:i32 = 0;

    loop {
        for line in input.lines() {
            freq += line.parse::<i32>().expect("Bad number");
            if freqs.contains(&freq) {
                println!("{}", freq);
                return
            }
            freqs.insert(freq);
        } 
    }
}