use std::collections::HashSet;  

pub fn p1(input: &String) -> i32 {
    let mut freq:i32 = 0;
    for line in input.lines() {
        freq += line.parse::<i32>().expect("Bad number");
    }
    return freq
}

pub fn p2(input: &String) -> i32 {
    let mut freqs_seen = HashSet::new();
    let mut freq_curr:i32 = 0;

    let freqs: Vec<i32> = input.split_terminator('\n')
                               .map(|x: &str| x.parse()
                                               .expect("Bad number"))
                               .collect();

    freqs_seen.insert(0);

    loop {
        for freq in &freqs {
            freq_curr += freq;
            if freqs_seen.contains(&freq_curr) {
                return freq_curr
            }
            freqs_seen.insert(freq_curr);
        } 
    }
}