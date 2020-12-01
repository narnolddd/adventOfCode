// use std::env;
use std::io::{self, BufRead}; 
use std::collections::HashMap;


fn main() {
    let stdin = io::stdin();
    let mut values = HashMap::new();
    
    for line in stdin.lock().lines() {
        let v: u32 = match line.unwrap().trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };
        values.insert(v, 2020 - v);
    }
    
    for (key, value) in &values {
        match values.get(value) {
            Some(_) => {
                println!("{} {} {}", key, value, key * value);
                break;
            },
            None => continue

        }
    }

    // Part 2
    let mut second_map = HashMap::new();
    for (k1, _) in &values {
        for (k2, _) in & values {
            if k1 == k2 || k1 + k2 > 2020 {
                continue
            }
           let v = k1 + k2;
           let key = (k1, k2, 2020 - v);
           second_map.insert(key, 2020 - v);
        }
    }


     for (key, value) in &second_map {
        match values.get(value) {
            Some(_) => {
                println!("{} {} {} {}", key.0, key.1, value, key.0 * key.1 * value);
                break;
            },
            None => continue
        }
    }
}