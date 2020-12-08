use std::io::{self, BufRead}; 
use std::collections::HashMap;
use std::process;

fn split_two(line: String) -> (String,  String) {
    let mut iter = line.splitn(2, ' ');
    let instruction = iter.next().unwrap();
    let options = iter.next().unwrap();
    (instruction.to_string(), options.to_string())

}

fn str_to_int(str: String) -> i32 {
    let int_string: i32 = match str.parse() {
        Ok(num) => num,
        Err(_) => {
            println!("Not a valid number {:?}", str);
            process::exit(1)
        }
    };
    int_string
}

fn parse_instructions(stdin: io::Stdin) -> Vec<(String, i32)> {
    let mut instructions = Vec::new();
    for line in stdin.lock().lines() {
        let (instruction, value) = split_two(line.unwrap().trim().to_string());
        let value = str_to_int(value);
        instructions.push( (instruction, value) )
    }
    instructions
}

fn run_instruction(inst: &(String, i32), acc: i32, pc: i32) -> (i32, i32) {
    let (cmd, value) = inst;
    match cmd.as_str() {
        "acc" => (acc + value, pc + 1),
        "jmp" => (acc, pc + value),
        "nop" => (acc, pc + 1),
        _ => { 
            println!("Unknown instruction");
            (acc, pc + 1)
        },
    }
}

fn main() {
    let stdin = io::stdin();
    let mut executed = HashMap::new();
    let mut exec_stack = Vec::new();
    let mut acc: i32 = 0;
    let mut pc: i32 = 0;
    let instructions = parse_instructions(stdin);
    let mut inst = instructions[pc as usize].clone();
    let mut rewind =  false;
    loop {
        let (new_acc, new_pc) = run_instruction(&inst, acc, pc);
        
        if !rewind {
            exec_stack.push((pc, acc));
        }

        executed.insert(pc, true);
        match executed.get(&new_pc){
            Some(_) => {
                if !rewind {
                    // Part 1 Answer
                    println!("{:?}", acc);
                }

                rewind = true;
                // Return to previous instruction
                let (prev_pc, prev_acc) = exec_stack.pop().unwrap();
                pc = prev_pc;
                acc = prev_acc;
                inst = instructions[pc as usize].clone();
                
                if inst.0 == "jmp"{
                    inst = ("nop".to_string(), inst.1);
                } else if inst.0 == "nop" {
                    inst = ("jmp".to_string(), inst.1);
                }
                executed.remove(&new_pc);

            },
            None => { 
                    acc = new_acc;
                    pc = new_pc;
                    if pc >= instructions.len() as i32 {
                        break;
                    }
                    inst = instructions[pc as usize].clone();
            },
        };
    }
    
    println!("{:?}", acc);
}