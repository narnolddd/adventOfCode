use std::io::{self, BufRead};
use std::convert::TryInto;
use std::process;


fn str_to_int(str: String) -> u32 {
    let int_string: u32 = match str.parse() {
        Ok(num) => num,
        Err(_) => {
            println!("Not a valid number{:?}", str);
            process::exit(1)
        }
    };
    int_string
}

fn solve(password: String, chr: String, lbound: u32, ubound: u32) -> (u32, u32) {
    let mut rule1 = 0;
    let mut rule2 = 0;
    let lower = lbound.try_into().unwrap();
    let upper = ubound.try_into().unwrap();
    let count = password.matches(&chr).count();
    let byte_password = password.as_bytes();
    let byte_char = chr.as_bytes()[0];

    if count >= lower && count <= upper {
        rule1 = 1
    }

    if (byte_password[lower-1] == byte_char && 
        byte_password[upper-1] != byte_char) || 
       (byte_password[lower-1] != byte_char && 
        byte_password[upper-1] == byte_char){
        rule2 += 1
    }

    (rule1, rule2)
}

fn main() {
    let stdin = io::stdin();
    let mut rule1 = 0;
    let mut rule2 = 0;
    for line in stdin.lock().lines() {
        let line_string = line.unwrap();
        let parts: Vec<&str> = line_string.split_whitespace().collect();
        
        let bounds: Vec<&str> = parts[0].split("-").collect();
        let lower_bound = str_to_int(bounds[0].to_string());
        let upper_bound = str_to_int(bounds[1].to_string());

        let password = parts[2].to_string();
        let chr = parts[1][0..1].to_string();

        let solution = solve(password, chr, lower_bound, upper_bound);
        rule1 += solution.0;
        rule2 += solution.1;
        
    }
    println!("{} {} ", rule1, rule2);
}