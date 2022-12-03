use std::fs;
use std::io::Error;

fn read(path: String) -> Result<String, Error> {
    let input = fs::read_to_string(path)?;
    return Ok(input);
}
#[allow(dead_code)]
pub fn p1() -> i32 {
    let input = read("src/aoc2022/day1/input.txt".to_string()).expect("error from read");

    let mut max_kal: i32 = 0;
    let mut local_kal: i32 = 0;

    for line in input.lines() {
        if line == "" {
            if local_kal > max_kal {
                max_kal = local_kal;
            }
            local_kal = 0;
        } else {
            let kal: i32 = line.parse().unwrap();
            local_kal = local_kal + kal;
        }
    }

    return max_kal;
}

#[allow(dead_code)]
pub fn p2() -> i32 {
    let input = read("src/aoc2022/day1/input.txt".to_string()).expect("error from read");

    let mut max_kal1: i32 = 0;
    let mut max_kal2: i32 = 0;
    let mut max_kal3: i32 = 0;
    let mut local_kal: i32 = 0;

    for line in input.lines() {
        if line == "" {
            if local_kal > max_kal3 && local_kal > max_kal2 && local_kal > max_kal1 {
                max_kal1 = max_kal2;
                max_kal2 = max_kal3;
                max_kal3 = local_kal;
            } else if local_kal > max_kal2 && local_kal > max_kal1 {
                max_kal1 = max_kal2;
                max_kal2 = local_kal;
            } else if local_kal > max_kal1 {
                max_kal1 = local_kal;
            }
            local_kal = 0;
        } else {
            let kal: i32 = line.parse().unwrap();
            local_kal = local_kal + kal;
        }
    }

    if local_kal > max_kal3 && local_kal > max_kal2 && local_kal > max_kal1 {
        max_kal1 = max_kal2;
        max_kal2 = max_kal3;
        max_kal3 = local_kal;
    } else if local_kal > max_kal2 && local_kal > max_kal1 {
        max_kal1 = max_kal2;
        max_kal2 = local_kal;
    } else if local_kal > max_kal1 {
        max_kal1 = local_kal;
    }

    return max_kal1 + max_kal2 + max_kal3;
}

#[allow(dead_code)]
pub fn p2_2() -> i32 {
    let input = read("src/aoc2022/day1/input.txt".to_string()).expect("error from read");
    let mut elvs: Vec<i32> = vec![];

    for elv in input.split("\n\n") {
        let mut kal_elv: i32 = 0;

        for kal_str in elv.lines() {
            let kal: i32 = kal_str.parse().unwrap();
            kal_elv = kal_elv + kal;
        }
        elvs.push(kal_elv);
    }
    elvs.sort_by(|a, b| b.cmp(a));

    return elvs[0..3].iter().sum();
}
