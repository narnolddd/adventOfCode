use std::env;
use std::fs;
use std::char;
use std::process;
use std::io;

fn main() {
    // --snip--
	let filename ="Puzzle25.txt";
    println!("In file {}", filename);

    let contents = fs::read_to_string(filename)
        .expect("Something went wrong reading the file");
	
	

	let mut opCodes = Vec::new();
	let stringSplit = contents.split(',');
	let mut index = 0;
	let mut firstOutput=0;
	let mut secondOutput=0;
	let sSplit = contents.split(',');
	let mut relativeBase=0;
	let mut index=0;
	let mut inputBuffer=Vec::new();
	for s in sSplit
	{
		if s.parse::<i64>().is_ok()
		{
			opCodes.push(s.parse::<i64>().unwrap())
		}
	}
	//println!("Opcode length:{}",opCodes.len());
	for x in 0..10000//Create additional opCode memory
	{
		opCodes.push(0);
	}
	'outer: loop
	{
		//println!("OpCode:{}",opCodes[index]);
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
			let mut input = 0;
			if inputBuffer.len()==0
			{
				let mut inputS = String::new();
				match io::stdin().read_line(&mut inputS) 
				{
					Ok(n) => 
					{
						println!("{} bytes read", n);
						println!("{}", inputS);
						for c in inputS.chars()
						{
							if (c as u8)!=13
							{
								inputBuffer.push(c as u8);
							}
						}
					}
					Err(error) => println!("error: {}", error),
				}
			}
			input=*inputBuffer.get(0).unwrap();
			inputBuffer.remove(0);
			println!("Input:{}",input as i64);
			let outputPosition = opCodes[index+1] as usize;
			opCodes[outputPosition]=input as i64;
			//println!("Input:{}",input);
			index+=2;
		}
		else if opCodes[index]==4
		{
			let outputPosition = opCodes[index+1] as usize;
			//println!("Output:{}",opCodes[outputPosition]);
			firstOutput=opCodes[outputPosition];
			let mut cOutput=firstOutput as u8;
			let mut cOutput2=cOutput as char;
			print!("{}",cOutput2);
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
		else if opCodes[index]==201
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=(relativeBase+opCodes[index+1]) as usize;
			let inputPosition2=opCodes[index+2] as usize;
			opCodes[outputPosition]=opCodes[inputPosition1]+opCodes[inputPosition2];
			index+=4;
		}
		else if opCodes[index]==2001
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=opCodes[index+1] as usize;
			let inputPosition2=(relativeBase+opCodes[index+2]) as usize;
			opCodes[outputPosition]=opCodes[inputPosition1]+opCodes[inputPosition2];
			index+=4;
		}
		else if opCodes[index]==2201
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=(relativeBase+opCodes[index+1]) as usize;
			let inputPosition2=(relativeBase+opCodes[index+2]) as usize;
			opCodes[outputPosition]=opCodes[inputPosition1]+opCodes[inputPosition2];
			index+=4;
		}
		else if opCodes[index]==2101
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=opCodes[index+1];
			let inputPosition2=(relativeBase+opCodes[index+2]) as usize;
			opCodes[outputPosition]=inputPosition1+opCodes[inputPosition2];
			index+=4;
		}
		else if opCodes[index]==1201
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=(relativeBase+opCodes[index+1]) as usize;
			let inputPosition2=opCodes[index+2];
			opCodes[outputPosition]=opCodes[inputPosition1]+inputPosition2;
			index+=4;
		}
		else if opCodes[index]==21101
		{
			let outputPosition = (relativeBase+opCodes[index+3]) as usize;
			let inputPosition1=opCodes[index+1];
			let inputPosition2=opCodes[index+2];
			opCodes[outputPosition]=inputPosition1+inputPosition2;
			index+=4;
		}
		else if opCodes[index]==21201
		{
			let outputPosition = (relativeBase+opCodes[index+3]) as usize;
			let inputPosition1=(relativeBase+opCodes[index+1]) as usize;
			let inputPosition2=opCodes[index+2];
			opCodes[outputPosition]=opCodes[inputPosition1]+inputPosition2;
			index+=4;
		}
		else if opCodes[index]==22101
		{
			let outputPosition = (relativeBase+opCodes[index+3]) as usize;
			let inputPosition1=opCodes[index+1];
			let inputPosition2=(relativeBase+opCodes[index+2]) as usize;
			opCodes[outputPosition]=inputPosition1+opCodes[inputPosition2];
			index+=4;
		}
		else if opCodes[index]==22201
		{
			let outputPosition = (relativeBase+opCodes[index+3]) as usize;
			let inputPosition1=(relativeBase+opCodes[index+1]) as usize;
			let inputPosition2=(relativeBase+opCodes[index+2]) as usize;
			opCodes[outputPosition]=opCodes[inputPosition1]+opCodes[inputPosition2];
			index+=4;
		}
		else if opCodes[index]==21001
		{
			let outputPosition = (relativeBase+opCodes[index+3]) as usize;
			let inputPosition1=opCodes[index+1] as usize;
			let inputPosition2=opCodes[index+2];
			opCodes[outputPosition]=opCodes[inputPosition1]+inputPosition2;
			index+=4;
		}
		else if opCodes[index]==20101
		{
			let outputPosition = (relativeBase+opCodes[index+3]) as usize;
			let inputPosition1=opCodes[index+1];
			let inputPosition2=opCodes[index+2] as usize;
			opCodes[outputPosition]=inputPosition1+opCodes[inputPosition2];
			index+=4;
		}
		else if opCodes[index]==22001
		{
			let outputPosition = (relativeBase+opCodes[index+3]) as usize;
			let inputPosition1=opCodes[index+1] as usize;
			let inputPosition2=(relativeBase+opCodes[index+2]) as usize;
			opCodes[outputPosition]=opCodes[inputPosition1]+opCodes[inputPosition2];
			index+=4;
		}
		else if opCodes[index]==20001
		{
			let outputPosition = (relativeBase+opCodes[index+3]) as usize;
			let inputPosition1=opCodes[index+1] as usize;
			let inputPosition2=opCodes[index+2] as usize;
			opCodes[outputPosition]=opCodes[inputPosition1]+opCodes[inputPosition2];
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
		else if opCodes[index]==202
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=(relativeBase+opCodes[index+1]) as usize;
			let inputPosition2=opCodes[index+2] as usize;
			opCodes[outputPosition]=opCodes[inputPosition1]*opCodes[inputPosition2];
			index+=4;
		}
		else if opCodes[index]==2002
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=opCodes[index+1] as usize;
			let inputPosition2=(relativeBase+opCodes[index+2]) as usize;
			opCodes[outputPosition]=opCodes[inputPosition1]*opCodes[inputPosition2];
			index+=4;
		}
		else if opCodes[index]==2202
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=(relativeBase+opCodes[index+1]) as usize;
			let inputPosition2=(relativeBase+opCodes[index+2]) as usize;
			opCodes[outputPosition]=opCodes[inputPosition1]*opCodes[inputPosition2];
			index+=4;
		}
		else if opCodes[index]==2102
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=opCodes[index+1];
			let inputPosition2=(relativeBase+opCodes[index+2]) as usize;
			opCodes[outputPosition]=inputPosition1*opCodes[inputPosition2];
			index+=4;
		}
		else if opCodes[index]==1202
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=(relativeBase+opCodes[index+1]) as usize;
			let inputPosition2=opCodes[index+2];
			opCodes[outputPosition]=opCodes[inputPosition1]*inputPosition2;
			index+=4;
		}
		else if opCodes[index]==21102
		{
			let outputPosition = (relativeBase+opCodes[index+3]) as usize;
			let inputPosition1=opCodes[index+1];
			let inputPosition2=opCodes[index+2];
			opCodes[outputPosition]=inputPosition1*inputPosition2;
			index+=4;
		}
		else if opCodes[index]==22102
		{
			let outputPosition = (relativeBase+opCodes[index+3]) as usize;
			let inputPosition1=opCodes[index+1];
			let inputPosition2=(relativeBase+opCodes[index+2]) as usize;
			opCodes[outputPosition]=inputPosition1*opCodes[inputPosition2];
			index+=4;
		}
		else if opCodes[index]==21202
		{
			let outputPosition = (relativeBase+opCodes[index+3]) as usize;
			let inputPosition1=(relativeBase+opCodes[index+1]) as usize;
			let inputPosition2=opCodes[index+2];
			opCodes[outputPosition]=opCodes[inputPosition1]*inputPosition2;
			index+=4;
		}
		else if opCodes[index]==22202
		{
			let outputPosition = (relativeBase+opCodes[index+3]) as usize;
			let inputPosition1=(relativeBase+opCodes[index+1]) as usize;
			let inputPosition2=(relativeBase+opCodes[index+2]) as usize;
			opCodes[outputPosition]=opCodes[inputPosition1]*opCodes[inputPosition2];
			index+=4;
		}
		else if opCodes[index]==21002
		{
			let outputPosition = (relativeBase+opCodes[index+3]) as usize;
			let inputPosition1=opCodes[index+1] as usize;
			let inputPosition2=opCodes[index+2];
			opCodes[outputPosition]=opCodes[inputPosition1]*inputPosition2;
			index+=4;
		}
		else if opCodes[index]==20102
		{
			let outputPosition = (relativeBase+opCodes[index+3]) as usize;
			let inputPosition1=opCodes[index+1];
			let inputPosition2=opCodes[index+2] as usize;
			opCodes[outputPosition]=inputPosition1*opCodes[inputPosition2];
			index+=4;
		}
		else if opCodes[index]==22002
		{
			let outputPosition = (relativeBase+opCodes[index+3]) as usize;
			let inputPosition1=opCodes[index+1] as usize;
			let inputPosition2=(relativeBase+opCodes[index+2]) as usize;
			opCodes[outputPosition]=opCodes[inputPosition1]*opCodes[inputPosition2];
			index+=4;
		}
		else if opCodes[index]==20002
		{
			let outputPosition = (relativeBase+opCodes[index+3]) as usize;
			let inputPosition1=opCodes[index+1] as usize;
			let inputPosition2=opCodes[index+2] as usize;
			opCodes[outputPosition]=opCodes[inputPosition1]*opCodes[inputPosition2];
			index+=4;
		}
		else if opCodes[index]==104
		{
			let outputPosition = opCodes[index+1];
			//println!("Output:{}",outputPosition);
			firstOutput=outputPosition;
			let mut cOutput=firstOutput as u8;
			let mut cOutput2=cOutput as char;
			print!("{}",cOutput2);
			index+=2;
		}
		else if opCodes[index]==204
		{
			let outputPosition = (opCodes[index+1]+relativeBase) as usize;
			//println!("Output:{}",opCodes[outputPosition]);
			firstOutput=opCodes[outputPosition];
			let mut cOutput=firstOutput as u8;
			let mut cOutput2=cOutput as char;
			print!("{}",cOutput2);
			index+=2;
		}
		else if opCodes[index]==203
		{
			let mut input = 0;
			//println!("Input:{}",input);
			if inputBuffer.len()==0
			{
				let mut inputS = String::new();
				match io::stdin().read_line(&mut inputS) 
				{
					Ok(n) => 
					{
						println!("{} bytes read", n);
						println!("{}", inputS);
						for c in inputS.chars()
						{
							if (c as u8)!=13
							{
								inputBuffer.push(c as u8);
							}
						}
					}
					Err(error) => println!("error: {}", error),
				}
			}
			input=*inputBuffer.get(0).unwrap();
			inputBuffer.remove(0);
			println!("Input:{}",input as i64);
			let outputPosition = (relativeBase+opCodes[index+1]) as usize;
			opCodes[outputPosition]=input as i64;
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
		else if opCodes[index]==205
		{
			let inputPosition=(relativeBase+opCodes[index+1]) as usize;
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
		else if opCodes[index]==2005
		{
			let inputPosition=opCodes[index+1] as usize;
			let jumpPosition=(relativeBase+opCodes[index+2]) as usize;
			if opCodes[inputPosition]!=0
			{
				index=opCodes[jumpPosition] as usize;
			}
			else
			{
				index+=3;
			}
		}
		else if opCodes[index]==2205
		{
			let inputPosition=(relativeBase+opCodes[index+1]) as usize;
			let jumpPosition=(relativeBase+opCodes[index+2]) as usize;
			if opCodes[inputPosition]!=0
			{
				index=opCodes[jumpPosition] as usize;
			}
			else
			{
				index+=3;
			}
		}
		else if opCodes[index]==2105
		{
			let inputPosition=opCodes[index+1] as usize;
			let jumpPosition=(relativeBase+opCodes[index+2]) as usize;
			if inputPosition!=0
			{
				index=opCodes[jumpPosition] as usize;
			}
			else
			{
				index+=3;
			}
		}
		else if opCodes[index]==1205
		{
			let inputPosition=(relativeBase+opCodes[index+1]) as usize;
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
		else if opCodes[index]==206
		{
			let inputPosition=(relativeBase+opCodes[index+1]) as usize;
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
		else if opCodes[index]==2006
		{
			let inputPosition=opCodes[index+1] as usize;
			let jumpPosition=(relativeBase+opCodes[index+2]) as usize;
			if opCodes[inputPosition]==0
			{
				index=opCodes[jumpPosition] as usize;
			}
			else
			{
				index+=3;
			}
		}
		else if opCodes[index]==2206
		{
			let inputPosition=(relativeBase+opCodes[index+1]) as usize;
			let jumpPosition=(relativeBase+opCodes[index+2]) as usize;
			if opCodes[inputPosition]==0
			{
				index=opCodes[jumpPosition] as usize;
			}
			else
			{
				index+=3;
			}
		}
		else if opCodes[index]==2106
		{
			let inputPosition=opCodes[index+1] as usize;
			let jumpPosition=(relativeBase+opCodes[index+2]) as usize;
			if inputPosition==0
			{
				index=opCodes[jumpPosition] as usize;
			}
			else
			{
				index+=3;
			}
		}
		else if opCodes[index]==1206
		{
			let inputPosition=(relativeBase+opCodes[index+1]) as usize;
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
		else if opCodes[index]==207
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=(relativeBase+opCodes[index+1]) as usize;
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
		else if opCodes[index]==2007
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=opCodes[index+1] as usize;
			let inputPosition2=(relativeBase+opCodes[index+2]) as usize;
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
		else if opCodes[index]==2207
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=(relativeBase+opCodes[index+1]) as usize;
			let inputPosition2=(relativeBase+opCodes[index+2]) as usize;
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
		else if opCodes[index]==2107
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=opCodes[index+1];
			let inputPosition2=(relativeBase+opCodes[index+2]) as usize;
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
		else if opCodes[index]==1207
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=(relativeBase+opCodes[index+1]) as usize;
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
		else if opCodes[index]==21107
		{
			let outputPosition = (relativeBase+opCodes[index+3]) as usize;
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
		else if opCodes[index]==21207
		{
			let outputPosition = (relativeBase+opCodes[index+3]) as usize;
			let inputPosition1=(relativeBase+opCodes[index+1]) as usize;
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
		else if opCodes[index]==22107
		{
			let outputPosition = (relativeBase+opCodes[index+3]) as usize;
			let inputPosition1=opCodes[index+1];
			let inputPosition2=(relativeBase+opCodes[index+2]) as usize;
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
		else if opCodes[index]==22207
		{
			let outputPosition = (relativeBase+opCodes[index+3]) as usize;
			let inputPosition1=(relativeBase+opCodes[index+1]) as usize;
			let inputPosition2=(relativeBase+opCodes[index+2]) as usize;
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
		else if opCodes[index]==20207
		{
			let outputPosition = (relativeBase+opCodes[index+3]) as usize;
			let inputPosition1=(relativeBase+opCodes[index+1]) as usize;
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
		else if opCodes[index]==22007
		{
			let outputPosition = (relativeBase+opCodes[index+3]) as usize;
			let inputPosition1=opCodes[index+1] as usize;
			let inputPosition2=(relativeBase+opCodes[index+2]) as usize;
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
		else if opCodes[index]==21007
		{
			let outputPosition = (relativeBase+opCodes[index+3]) as usize;
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
		else if opCodes[index]==20107
		{
			let outputPosition = (relativeBase+opCodes[index+3]) as usize;
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
		else if opCodes[index]==208
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=(relativeBase+opCodes[index+1]) as usize;
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
		else if opCodes[index]==2008
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=opCodes[index+1] as usize;
			let inputPosition2=(relativeBase+opCodes[index+2]) as usize;
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
		else if opCodes[index]==2208
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=(relativeBase+opCodes[index+1]) as usize;
			let inputPosition2=(relativeBase+opCodes[index+2]) as usize;
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
		else if opCodes[index]==2108
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=opCodes[index+1];
			let inputPosition2=(relativeBase+opCodes[index+2]) as usize;
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
		else if opCodes[index]==1208
		{
			let outputPosition = opCodes[index+3] as usize;
			let inputPosition1=(relativeBase+opCodes[index+1]) as usize;
			let inputPosition2=opCodes[index+2];
			if opCodes[inputPosition1]==inputPosition2
			{
				opCodes[outputPosition]=1;
			}
			else
			{
				opCodes[outputPosition]=0;
				opCodes[outputPosition]=0;
			}
			index+=4;
		}
		else if opCodes[index]==21108
		{
			let outputPosition = (relativeBase+opCodes[index+3]) as usize;
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
		else if opCodes[index]==20208//Check Puzzle 17 error here
		{
			let outputPosition = (relativeBase+opCodes[index+3]) as usize;
			let inputPosition1=(relativeBase+opCodes[index+1]) as usize;
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
		else if opCodes[index]==22208
		{
			let outputPosition = (relativeBase+opCodes[index+3]) as usize;
			let inputPosition1=(relativeBase+opCodes[index+1]) as usize;
			let inputPosition2=(relativeBase+opCodes[index+2]) as usize;
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
		else if opCodes[index]==21208
		{
			let outputPosition = (relativeBase+opCodes[index+3]) as usize;
			let inputPosition1=(relativeBase+opCodes[index+1]) as usize;
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
		else if opCodes[index]==20008
		{
			let outputPosition = (relativeBase+opCodes[index+3]) as usize;
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
		else if opCodes[index]==21008
		{
			let outputPosition = (relativeBase+opCodes[index+3]) as usize;
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
		else if opCodes[index]==9
		{
			let inputPosition1=opCodes[index+1] as usize;
			relativeBase+=opCodes[inputPosition1];
			index+=2;
		}
		else if opCodes[index]==109
		{
			let inputPosition1=opCodes[index+1];
			relativeBase+=inputPosition1;
			index+=2;
		}
		else if opCodes[index]==209
		{
			let inputPosition1=(relativeBase+opCodes[index+1]) as usize;
			relativeBase+=opCodes[inputPosition1];
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
	
	println!("First Anwser :\n{}",firstOutput);

	
	
	println!("Second Anwser :\n{}",firstOutput);
	
	
}
