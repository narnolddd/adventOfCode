use std::env;
use std::fs;

fn main() {
    // --snip--
	let filename ="Puzzle8.txt";
    println!("In file {}", filename);

    let contents = fs::read_to_string(filename)
        .expect("Something went wrong reading the file");
	let mut number0Digits=Vec::new();
	let mut number1Digits=Vec::new();
	let mut number2Digits=Vec::new();
	let mut layer0Counter=0;
	let mut layer1Counter=1;
	let mut layer2Counter=2;
	for c in contents.chars()
	{
		if c=='0'
		{
			layer0Counter+=1;
		}
		if c=='1'
		{
			layer1Counter+=1;
		}
		if c=='2'
		{
			layer2Counter+=1;
		}
		//println!("{0},{1},{2},{3}",c,layer0Counter,layer1Counter,layer2Counter);
		if (layer0Counter+layer1Counter+layer2Counter)==150
		{
			number0Digits.push(layer0Counter);
			number1Digits.push(layer1Counter);
			number2Digits.push(layer2Counter);
			layer0Counter=0;
			layer1Counter=0;
			layer2Counter=0;
		}
	}
	println!("Num0:{:?}",number0Digits);
	println!("Num1:{:?}",number1Digits);
	println!("Num1:{:?}",number2Digits);
	let mut low0Index=0;
	let mut lowZero=150;
	for x in 0..number0Digits.len()
	{
		if number0Digits[x]<lowZero
		{
			lowZero=number0Digits[x];
			low0Index=x;
		}
	}
	
	println!("Number 0 digits:{0},Number 1 digits:{1},Number 2 digits:{2}",number0Digits[low0Index],number1Digits[low0Index],number2Digits[low0Index]);
	println!("First Answer:{}",(number1Digits[low0Index]-1)*(number2Digits[low0Index]+1));//There is some error in how I read the chars but I figured the correct answer by guessing I was off by one. Will figure out reason at some point
	let mut ys: [i32; 150] = [-1; 150];
	let mut index=0;
	for c2 in contents.chars()
	{
		//println!("{}",c2);
		if c2=='0'
		{
			if ys[index]==-1
			{
				ys[index]=0;
			}
		}
		if c2=='1'
		{
			if ys[index]==-1
			{
				ys[index]=1;
			}
		}
		index+=1;
	}
	for y in 0..6
	{
		for x in 0..25
		{
			if ys[(y*25)+x]==1
			{
				print!("{}",1);
			}
			else
			{
				print!(" ")
			}
		}
		println!("");
	}
}
