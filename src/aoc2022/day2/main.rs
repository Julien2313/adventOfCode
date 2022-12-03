use std::collections::HashMap;
use std::fs;
use std::io::Error;

fn read(path: String) -> Result<String, Error> {
    let input = fs::read_to_string(path)?;
    return Ok(input);
}

#[allow(dead_code)]
pub fn p1() -> i32 {
    let input = read("src/aoc2022/day2/input.txt".to_string()).expect("error from read");

    let mut values = HashMap::new();

    values.insert("A", 0);
    values.insert("B", 1);
    values.insert("C", 2);
    values.insert("X", 0);
    values.insert("Y", 1);
    values.insert("Z", 2);

    let mut score: i32 = 0;

    for line in input.lines() {
        let vec = line.split_whitespace().collect::<Vec<&str>>();
        let you = *values.get(&vec[0]).unwrap();
        let me = *values.get(&vec[1]).unwrap();

        score = score + me + 1;
        if you == me {
            score = score + 3;
        } else if (you + 1) % 3 == me {
            score = score + 6;
        }
    }

    return score;
}

#[allow(dead_code)]
pub fn p2() -> i32 {
    let input = read("src/aoc2022/day2/input.txt".to_string()).expect("error from read");

    let mut values = HashMap::new();

    values.insert("A", 0); //rock
    values.insert("B", 1); //paper
    values.insert("C", 2); //scisors
    values.insert("X", 0); //lose
    values.insert("Y", 1); //draw
    values.insert("Z", 2); //win

    let mut score: i32 = 0;

    for line in input.lines() {
        let vec = line.split_whitespace().collect::<Vec<&str>>();
        let you = *values.get(&vec[0]).unwrap();
        let result = *values.get(&vec[1]).unwrap();

        if result == 2 {
            let choice: i32 = you + 1;
            score = score + choice.rem_euclid(3) + 6 + 1;
        } else if result == 0 {
            let choice: i32 = you - 1;
            score = score + choice.rem_euclid(3) + 1;
        } else {
            score = score + you + 3 + 1;
        }
    }

    return score;
}
