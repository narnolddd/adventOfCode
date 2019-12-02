use std::env;
use std::fs;

fn main() {
    // --snip--
	let filename ="Puzzle2.txt";
    println!("In file {}", filename);

    let contents = fs::read_to_string(filename)
        .expect("Something went wrong reading the file");
	let mut opCodes = Vec::new();
	let stringSplit = contents.split(',');
	let mut index = 0;
	for s in stringSplit
	{
		if s.parse::<u32>().is_ok()
		{
			opCodes.push(s.parse::<u32>().unwrap())
		}
	}
	println!("Test :\n{}",opCodes[index]);
	opCodes[1]=12;
	opCodes[2]=2;
	'outer: loop
	{
		if opCodes[index]==1
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=opCodes[index+1] as usize;
			let inputPosition2=opCodes[index+2] as usize;
			opCodes[outputPosition]=opCodes[inputPosition1]+opCodes[inputPosition2];
		}
		if opCodes[index]==2
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=opCodes[index+1] as usize;
			let inputPosition2=opCodes[index+2] as usize;
			opCodes[outputPosition]=opCodes[inputPosition1]*opCodes[inputPosition2];
		}
		if opCodes[index]==99
		{
			break 'outer;
		}
		index+=4;
		println!("{:?}", opCodes);
	}
	println!("First Answer :\n{}",opCodes[0]);
	let mut noun =0;
	let mut verb =0;
	'outer1: loop
	{
		opCodes.clear();
		let sSplit = contents.split(',');
		for s in sSplit
		{
			if s.parse::<u32>().is_ok()
			{
				opCodes.push(s.parse::<u32>().unwrap())
			}
		}
		index=0;
		opCodes[1]=noun;
		opCodes[2]=verb;
		//println!("{:?}", opCodes);
		'inner: loop
		{
			if opCodes[index]==1
			{
				let outputPosition = opCodes[index+3] as usize;
				let inputPosition1=opCodes[index+1] as usize;
				let inputPosition2=opCodes[index+2] as usize;
				opCodes[outputPosition]=opCodes[inputPosition1]+opCodes[inputPosition2];
			}
			if opCodes[index]==2
			{
				let outputPosition = opCodes[index+3] as usize;
				let inputPosition1=opCodes[index+1] as usize;
				let inputPosition2=opCodes[index+2] as usize;
				opCodes[outputPosition]=opCodes[inputPosition1]*opCodes[inputPosition2];
			}
			if opCodes[index]==99
			{
				break 'inner;
			}
			index+=4;
			//println!("{:?}", opCodes);
		}
		if opCodes[0]==19690720
		{
			break 'outer1;
		}
		else
		{
			println!("Noun :\n{0},{1},{2}",noun,verb,opCodes[0]);
			if verb<99
			{
				verb+=1;
			}
			else
			{
				noun+=1;
				verb=0;
			}	
		}
	}
	println!("Noun :\n{}",noun);
	println!("Verb :\n{}",verb);
	println!("Second Anser :\n{}",noun*100+verb);

	
}