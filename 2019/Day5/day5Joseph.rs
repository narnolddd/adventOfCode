use std::env;
use std::fs;

fn main() {
    // --snip--
	let filename ="Puzzle5.txt";
    println!("In file {}", filename);

    let contents = fs::read_to_string(filename)
        .expect("Something went wrong reading the file");
	let mut opCodes = Vec::new();
	let stringSplit = contents.split(',');
	let mut index = 0;
	let mut firstOutput=0;
	let mut secondOutput=0;
	for s in stringSplit
	{
		if s.parse::<i32>().is_ok()
		{
			opCodes.push(s.parse::<i32>().unwrap())
		}
	}
	'outer: loop
	{
		if opCodes[index]==1
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=opCodes[index+1] as usize;
			let inputPosition2=opCodes[index+2] as usize;
			opCodes[outputPosition]=opCodes[inputPosition1]+opCodes[inputPosition2];
			index+=4;
		}
		else if opCodes[index]==2
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=opCodes[index+1] as usize;
			let inputPosition2=opCodes[index+2] as usize;
			opCodes[outputPosition]=opCodes[inputPosition1]*opCodes[inputPosition2];
			index+=4;
		}
		else if opCodes[index]==3
		{
			let input = 1;//Input defined in problem statement
			let outputPosition = opCodes[index+1] as usize;
			opCodes[outputPosition]=input;
			index+=2;
		}
		else if opCodes[index]==4
		{
			let outputPosition = opCodes[index+1] as usize;
			println!("Output:{}",opCodes[outputPosition]);
			firstOutput=opCodes[outputPosition];
			index+=2;
		}
		else if opCodes[index]==101
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=opCodes[index+1];
			let inputPosition2=opCodes[index+2] as usize;
			opCodes[outputPosition]=inputPosition1+opCodes[inputPosition2];
			index+=4;
		}
		else if opCodes[index]==1001
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=opCodes[index+1] as usize;
			let inputPosition2=opCodes[index+2];
			opCodes[outputPosition]=opCodes[inputPosition1]+inputPosition2;
			index+=4;
		}
		else if opCodes[index]==1101
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=opCodes[index+1];
			let inputPosition2=opCodes[index+2];
			opCodes[outputPosition]=inputPosition1+inputPosition2;
			index+=4;
		}
		else if opCodes[index]==102
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=opCodes[index+1];
			let inputPosition2=opCodes[index+2] as usize;
			opCodes[outputPosition]=inputPosition1*opCodes[inputPosition2];
			index+=4;
		}
		else if opCodes[index]==1002
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=opCodes[index+1] as usize;
			let inputPosition2=opCodes[index+2];
			opCodes[outputPosition]=opCodes[inputPosition1]*inputPosition2;
			index+=4;
		}
		else if opCodes[index]==1102
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=opCodes[index+1];
			let inputPosition2=opCodes[index+2];
			opCodes[outputPosition]=inputPosition1*inputPosition2;
			index+=4;
		}
		else if opCodes[index]==104
		{
			let outputPosition = opCodes[index+1];
			println!("Output:{}",outputPosition);
			firstOutput=outputPosition;
			index+=2;
		}
		else if opCodes[index]==99
		{
			break 'outer;
		}
		else
		{
			println!("Opcode error: {}",opCodes[index]);
			break 'outer;
			
		}
	}
	println!("First Answer :\n{}",firstOutput);
	index=0;
	opCodes.clear();
	let sSplit = contents.split(',');
	for s in sSplit
	{
		if s.parse::<i32>().is_ok()
		{
			opCodes.push(s.parse::<i32>().unwrap())
		}
	}
	'outer1: loop
	{
		if opCodes[index]==1
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=opCodes[index+1] as usize;
			let inputPosition2=opCodes[index+2] as usize;
			opCodes[outputPosition]=opCodes[inputPosition1]+opCodes[inputPosition2];
			index+=4;
		}
		else if opCodes[index]==2
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=opCodes[index+1] as usize;
			let inputPosition2=opCodes[index+2] as usize;
			opCodes[outputPosition]=opCodes[inputPosition1]*opCodes[inputPosition2];
			index+=4;
		}
		else if opCodes[index]==3
		{
			let input = 5;//Input defined in problem statement
			let outputPosition = opCodes[index+1] as usize;
			opCodes[outputPosition]=input;
			index+=2;
		}
		else if opCodes[index]==4
		{
			let outputPosition = opCodes[index+1] as usize;
			println!("Output:{}",opCodes[outputPosition]);
			secondOutput=opCodes[outputPosition];
			index+=2;
		}
		else if opCodes[index]==101
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=opCodes[index+1];
			let inputPosition2=opCodes[index+2] as usize;
			opCodes[outputPosition]=inputPosition1+opCodes[inputPosition2];
			index+=4;
		}
		else if opCodes[index]==1001
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=opCodes[index+1] as usize;
			let inputPosition2=opCodes[index+2];
			opCodes[outputPosition]=opCodes[inputPosition1]+inputPosition2;
			index+=4;
		}
		else if opCodes[index]==1101
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=opCodes[index+1];
			let inputPosition2=opCodes[index+2];
			opCodes[outputPosition]=inputPosition1+inputPosition2;
			index+=4;
		}
		else if opCodes[index]==102
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=opCodes[index+1];
			let inputPosition2=opCodes[index+2] as usize;
			opCodes[outputPosition]=inputPosition1*opCodes[inputPosition2];
			index+=4;
		}
		else if opCodes[index]==1002
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=opCodes[index+1] as usize;
			let inputPosition2=opCodes[index+2];
			opCodes[outputPosition]=opCodes[inputPosition1]*inputPosition2;
			index+=4;
		}
		else if opCodes[index]==1102
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=opCodes[index+1];
			let inputPosition2=opCodes[index+2];
			opCodes[outputPosition]=inputPosition1*inputPosition2;
			index+=4;
		}
		else if opCodes[index]==104
		{
			let outputPosition = opCodes[index+1];
			println!("Output:{}",outputPosition);
			secondOutput=outputPosition;
			index+=2;
		}
		else if opCodes[index]==5//At this point I have begun to regret my decision to shamelessly brute force this but have decided to power on regardless
		{
			let inputPosition=opCodes[index+1] as usize;
			let jumpPosition=opCodes[index+2] as usize;
			if opCodes[inputPosition]!=0
			{
				index=opCodes[jumpPosition] as usize;
			}
			else
			{
				index+=3;
			}
		}
		else if opCodes[index]==105
		{
			let inputPosition=opCodes[index+1] as usize;
			let jumpPosition=opCodes[index+2] as usize;
			if inputPosition!=0
			{
				index=opCodes[jumpPosition] as usize;
			}
			else
			{
				index+=3;
			}
		}
		else if opCodes[index]==1005
		{
			let inputPosition=opCodes[index+1] as usize;
			let jumpPosition=opCodes[index+2] as usize;
			if opCodes[inputPosition]!=0
			{
				index=jumpPosition;
			}
			else
			{
				index+=3;
			}
		}
		else if opCodes[index]==1105
		{
			let inputPosition=opCodes[index+1] as usize;
			let jumpPosition=opCodes[index+2] as usize;
			if inputPosition!=0
			{
				index=jumpPosition;
			}
			else
			{
				index+=3;
			}
		}
		else if opCodes[index]==6
		{
			let inputPosition=opCodes[index+1] as usize;
			let jumpPosition=opCodes[index+2] as usize;
			if opCodes[inputPosition]==0
			{
				index=opCodes[jumpPosition] as usize;
			}
			else
			{
				index+=3;
			}
		}
		else if opCodes[index]==106
		{
			let inputPosition=opCodes[index+1] as usize;
			let jumpPosition=opCodes[index+2] as usize;
			if inputPosition==0
			{
				index=opCodes[jumpPosition] as usize;
			}
			else
			{
				index+=3;
			}
		}
		else if opCodes[index]==1006
		{
			let inputPosition=opCodes[index+1] as usize;
			let jumpPosition=opCodes[index+2] as usize;
			if opCodes[inputPosition]==0
			{
				index=jumpPosition;
			}
			else
			{
				index+=3;
			}
		}
		else if opCodes[index]==1106
		{
			let inputPosition=opCodes[index+1] as usize;
			let jumpPosition=opCodes[index+2] as usize;
			if inputPosition==0
			{
				index=jumpPosition;
			}
			else
			{
				index+=3;
			}
		}
		else if opCodes[index]==7
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=opCodes[index+1] as usize;
			let inputPosition2=opCodes[index+2] as usize;
			if opCodes[inputPosition1]<opCodes[inputPosition2]
			{
				opCodes[outputPosition]=1;
			}
			else
			{
				opCodes[outputPosition]=0;
			}
			index+=4;
		}
		else if opCodes[index]==107
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=opCodes[index+1];
			let inputPosition2=opCodes[index+2] as usize;
			if inputPosition1<opCodes[inputPosition2]
			{
				opCodes[outputPosition]=1;
			}
			else
			{
				opCodes[outputPosition]=0;
			}
			index+=4;
		}
		else if opCodes[index]==1007
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=opCodes[index+1] as usize;
			let inputPosition2=opCodes[index+2];
			if opCodes[inputPosition1]<inputPosition2
			{
				opCodes[outputPosition]=1;
			}
			else
			{
				opCodes[outputPosition]=0;
			}
			index+=4;
		}
		else if opCodes[index]==1107
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=opCodes[index+1];
			let inputPosition2=opCodes[index+2];
			if inputPosition1<inputPosition2
			{
				opCodes[outputPosition]=1;
			}
			else
			{
				opCodes[outputPosition]=0;
			}
			index+=4;
		}
		else if opCodes[index]==8
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=opCodes[index+1] as usize;
			let inputPosition2=opCodes[index+2] as usize;
			if opCodes[inputPosition1]==opCodes[inputPosition2]
			{
				opCodes[outputPosition]=1;
			}
			else
			{
				opCodes[outputPosition]=0;
			}
			index+=4;
		}
		else if opCodes[index]==108
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=opCodes[index+1];
			let inputPosition2=opCodes[index+2] as usize;
			if inputPosition1==opCodes[inputPosition2]
			{
				opCodes[outputPosition]=1;
			}
			else
			{
				opCodes[outputPosition]=0;
			}
			index+=4;
		}
		else if opCodes[index]==1008
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=opCodes[index+1] as usize;
			let inputPosition2=opCodes[index+2];
			if opCodes[inputPosition1]==inputPosition2
			{
				opCodes[outputPosition]=1;
			}
			else
			{
				opCodes[outputPosition]=0;
			}
			index+=4;
		}
		else if opCodes[index]==1108
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=opCodes[index+1];
			let inputPosition2=opCodes[index+2];
			if inputPosition1==inputPosition2
			{
				opCodes[outputPosition]=1;
			}
			else
			{
				opCodes[outputPosition]=0;
			}
			index+=4;
		}
		else if opCodes[index]==99
		{
			break 'outer1;
		}
		else
		{
			println!("Opcode error: {}",opCodes[index]);
			break 'outer1;
			
		}
	}


	println!("Second Answer :\n{}",secondOutput);

	
}
