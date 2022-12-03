use std::fs;
use std::io::Error;

fn read(path: String) -> Result<String, Error> {
    let input = fs::read_to_string(path)?;
    return Ok(input);
}

#[allow(dead_code)]
pub fn p1() -> i32 {
    let input = read("src/aoc2022/day3/input.txt".to_string()).expect("error from read");

    let alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    let mut scores: i32 = 0;

    for line in input.lines() {
        let mut score: i32 = 0;
        let (split1, split2) = line.split_at(line.len() / 2);
        let mut shared_char = String::from("");
        for c in split1.chars() {
            if split2.contains(c) && !shared_char.contains(c) {
                shared_char.push(c);
                score = score + (alphabet.find(c).unwrap() as i32) + 1;
            }
        }

        scores = scores + score;
    }

    return scores;
}

#[allow(dead_code)]
pub fn p2() -> i32 {
    let input = read("src/aoc2022/day3/input.txt".to_string()).expect("error from read");

    let alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    let mut scores: i32 = 0;

    let mut num_line: i32 = 0;
    let mut shared_char1 = String::from("");
    let mut shared_char2 = String::from("");

    for line in input.lines() {
        if num_line % 3 == 0 {
            shared_char1 = String::from("");
            shared_char2 = String::from("");
            for c in line.chars() {
                if !shared_char1.contains(c) {
                    shared_char1.push(c);
                }
            }
        } else if num_line % 3 == 1 {
            for c in line.chars() {
                if !shared_char2.contains(c) {
                    shared_char2.push(c);
                }
            }
        } else {
            for c in line.chars() {
                if shared_char1.contains(c) && shared_char2.contains(c) {
                    scores = scores + (alphabet.find(c).unwrap() as i32) + 1;
                    break;
                }
            }
        }

        num_line = num_line + 1
    }

    return scores;
}
