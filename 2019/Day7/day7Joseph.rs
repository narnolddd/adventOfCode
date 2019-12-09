use permutator::Permutation;
use std::fs;

fn main() {
	let mut data = vec![0, 1, 2,3,4];
	let filename ="Puzzle7.txt";
    println!("In file {}", filename);

    let contents = fs::read_to_string(filename)
        .expect("Something went wrong reading the file");
	let mut opCodes = Vec::new();
	let stringSplit = contents.split(',');
	let mut index = 0;
	let mut maxOutput=0;
	data.permutation().for_each(|p| 
	{

		println!("{:?}", p);
		let mut Output=0;
		//println!("{:?}", phaseArray);
		for pi in 0..5
		{
			opCodes.clear();
			let mut firstInput=true;
			let sSplit = contents.split(',');
			for s in sSplit
			{
				if s.parse::<i32>().is_ok()
				{
					opCodes.push(s.parse::<i32>().unwrap())
				}
			}
			index=0;
			'outer1: loop
			{
				//println!("Opcode:{:?}",opCodes);
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
					let mut input =0;
					if firstInput==true
					{
						input = p[pi];//Input defined in problem statement
					}
					else
					{
						input = Output;
					}
					let outputPosition = opCodes[index+1] as usize;
					opCodes[outputPosition]=input;
					firstInput=false;
					index+=2;
				}
				else if opCodes[index]==4
				{
					let outputPosition = opCodes[index+1] as usize;
					Output=opCodes[outputPosition];
					//println!("Output:{}",Output);
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
					Output+=outputPosition;
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
		}
		if Output>maxOutput
		{
			maxOutput=Output;
			println!("New max Output:{}",maxOutput);
			println!("Current Best Combination:{:?}",p);
		}
	});
	println!("First Answer :\n{}",maxOutput);
	let mut data2 = vec![5,6,7,8,9];
	maxOutput=0;
	index=0;
	data2.permutation().for_each(|p| 
	{
		let mut finalOutput=0;
		//println!("{:?}", p);
		let mut Output=0;
		let mut ampIndex=0;
		let sSplitA = contents.split(',');
		let mut opCodesA = Vec::new();
		for s in sSplitA
		{
			if s.parse::<i32>().is_ok()
			{
				opCodesA.push(s.parse::<i32>().unwrap())
			}
		}
		let sSplitB = contents.split(',');
		let mut opCodesB = Vec::new();
		for s in sSplitB
		{
			if s.parse::<i32>().is_ok()
			{
				opCodesB.push(s.parse::<i32>().unwrap())
			}
		}
		let sSplitC = contents.split(',');
		let mut opCodesC = Vec::new();
		for s in sSplitC
		{
			if s.parse::<i32>().is_ok()
			{
				opCodesC.push(s.parse::<i32>().unwrap())
			}
		}
		let sSplitD = contents.split(',');
		let mut opCodesD = Vec::new();
		for s in sSplitD
		{
			if s.parse::<i32>().is_ok()
			{
				opCodesD.push(s.parse::<i32>().unwrap())
			}
		}
		let sSplitE = contents.split(',');
		let mut opCodesE = Vec::new();
		for s in sSplitE
		{
			if s.parse::<i32>().is_ok()
			{
				opCodesE.push(s.parse::<i32>().unwrap())
			}
		}
		let mut codePosition=[0,0,0,0,0];
		//println!("{:?}",opCodes);
		
		
		let mut firstInput=[true,true,true,true,true];
		let mut curAmp=&mut opCodesA;
		'outer2:loop
		{
			//println!("Index:{0},Opcode:{1}",codePosition[ampIndex],curAmp[codePosition[ampIndex]]);
			/*for x in 0..5
			{
				print!("{},",codePosition[x]);
			}
			println!("");*/
			//println!("{:?}",opCodes);
			if curAmp[codePosition[ampIndex]]==1
			{
				let outputPosition = curAmp[codePosition[ampIndex]+3] as usize;
				let inputPosition1=curAmp[codePosition[ampIndex]+1] as usize;
				let inputPosition2=curAmp[codePosition[ampIndex]+2] as usize;
				curAmp[outputPosition]=curAmp[inputPosition1]+curAmp[inputPosition2];
				codePosition[ampIndex]+=4;
			}
			else if curAmp[codePosition[ampIndex]]==2
			{
				let outputPosition = curAmp[codePosition[ampIndex]+3] as usize;
				let inputPosition1=curAmp[codePosition[ampIndex]+1] as usize;
				let inputPosition2=curAmp[codePosition[ampIndex]+2] as usize;
				curAmp[outputPosition]=curAmp[inputPosition1]*curAmp[inputPosition2];
				codePosition[ampIndex]+=4;
			}
			else if curAmp[codePosition[ampIndex]]==3
			{
				let mut input =0;
				if firstInput[ampIndex]==true
				{
					input = p[ampIndex];//Input defined in problem statement
				}
				else
				{
					input = Output;
				}
				let outputPosition = curAmp[codePosition[ampIndex]+1] as usize;
				curAmp[outputPosition]=input;
				firstInput[ampIndex]=false;
				codePosition[ampIndex]+=2;
			}
			else if curAmp[codePosition[ampIndex]]==4
			{
				let outputPosition = curAmp[codePosition[ampIndex]+1] as usize;
				Output=curAmp[outputPosition];
				println!("Output:{}",Output);
				codePosition[ampIndex]+=2;
				ampIndex+=1;
				if ampIndex==5
				{
					finalOutput=Output;
					ampIndex=0;
				}
				match ampIndex 
				{
					0 => curAmp=&mut opCodesA,
					1 => curAmp=&mut opCodesB,
					2 => curAmp=&mut opCodesC,
					3 => curAmp=&mut opCodesD,
					4 => curAmp=&mut opCodesE,
					_ => println!("Amp Selection Error"),
				}
			}
			else if curAmp[codePosition[ampIndex]]==101
			{
				let outputPosition = curAmp[codePosition[ampIndex]+3] as usize;
				let inputPosition1=curAmp[codePosition[ampIndex]+1];
				let inputPosition2=curAmp[codePosition[ampIndex]+2] as usize;
				curAmp[outputPosition]=inputPosition1+curAmp[inputPosition2];
				codePosition[ampIndex]+=4;
			}
			else if curAmp[codePosition[ampIndex]]==1001
			{
				let outputPosition = curAmp[codePosition[ampIndex]+3] as usize;
				let inputPosition1=curAmp[codePosition[ampIndex]+1] as usize;
				let inputPosition2=curAmp[codePosition[ampIndex]+2];
				curAmp[outputPosition]=curAmp[inputPosition1]+inputPosition2;
				codePosition[ampIndex]+=4;
			}
			else if curAmp[codePosition[ampIndex]]==1101
			{
				let outputPosition = curAmp[codePosition[ampIndex]+3] as usize;
				let inputPosition1=curAmp[codePosition[ampIndex]+1];
				let inputPosition2=curAmp[codePosition[ampIndex]+2];
				curAmp[outputPosition]=inputPosition1+inputPosition2;
				codePosition[ampIndex]+=4;
			}
			else if curAmp[codePosition[ampIndex]]==102
			{
				let outputPosition = curAmp[codePosition[ampIndex]+3] as usize;
				let inputPosition1=curAmp[codePosition[ampIndex]+1];
				let inputPosition2=curAmp[codePosition[ampIndex]+2] as usize;
				curAmp[outputPosition]=inputPosition1*curAmp[inputPosition2];
				codePosition[ampIndex]+=4;
			}
			else if curAmp[codePosition[ampIndex]]==1002
			{
				let outputPosition = curAmp[codePosition[ampIndex]+3] as usize;
				let inputPosition1=curAmp[codePosition[ampIndex]+1] as usize;
				let inputPosition2=curAmp[codePosition[ampIndex]+2];
				curAmp[outputPosition]=curAmp[inputPosition1]*inputPosition2;
				codePosition[ampIndex]+=4;
			}
			else if curAmp[codePosition[ampIndex]]==1102
			{
				let outputPosition = curAmp[codePosition[ampIndex]+3] as usize;
				let inputPosition1=curAmp[codePosition[ampIndex]+1];
				let inputPosition2=curAmp[codePosition[ampIndex]+2];
				curAmp[outputPosition]=inputPosition1*inputPosition2;
				codePosition[ampIndex]+=4;
			}
			else if curAmp[codePosition[ampIndex]]==104
			{
				let outputPosition = curAmp[codePosition[ampIndex]+1];
				println!("Output:{}",outputPosition);
				Output+=outputPosition;
				codePosition[ampIndex]+=2;
				ampIndex+=1;
				if ampIndex==5
				{
					finalOutput=Output;
					ampIndex=0;
				}
			}
			else if curAmp[codePosition[ampIndex]]==5//At this point I have begun to regret my decision to shamelessly brute force this but have decided to power on regardless
			{
				let inputPosition=curAmp[codePosition[ampIndex]+1] as usize;
				let jumpPosition=curAmp[codePosition[ampIndex]+2] as usize;
				if curAmp[inputPosition]!=0
				{
					codePosition[ampIndex]=curAmp[jumpPosition] as usize;
				}
				else
				{
					codePosition[ampIndex]+=3;
				}
			}
			else if curAmp[codePosition[ampIndex]]==105
			{
				let inputPosition=curAmp[codePosition[ampIndex]+1] as usize;
				let jumpPosition=curAmp[codePosition[ampIndex]+2] as usize;
				if inputPosition!=0
				{
					codePosition[ampIndex]=curAmp[jumpPosition] as usize;
				}
				else
				{
					codePosition[ampIndex]+=3;
				}
			}
			else if curAmp[codePosition[ampIndex]]==1005
			{
				let inputPosition=curAmp[codePosition[ampIndex]+1] as usize;
				let jumpPosition=curAmp[codePosition[ampIndex]+2] as usize;
				if curAmp[inputPosition]!=0
				{
					codePosition[ampIndex]=jumpPosition;
				}
				else
				{
					codePosition[ampIndex]+=3;
				}
			}
			else if curAmp[codePosition[ampIndex]]==1105
			{
				let inputPosition=curAmp[codePosition[ampIndex]+1] as usize;
				let jumpPosition=curAmp[codePosition[ampIndex]+2] as usize;
				if inputPosition!=0
				{
					codePosition[ampIndex]=jumpPosition;
				}
				else
				{
					codePosition[ampIndex]+=3;
				}
			}
			else if curAmp[codePosition[ampIndex]]==6
			{
				let inputPosition=curAmp[codePosition[ampIndex]+1] as usize;
				let jumpPosition=curAmp[codePosition[ampIndex]+2] as usize;
				if curAmp[inputPosition]==0
				{
					codePosition[ampIndex]=curAmp[jumpPosition] as usize;
				}
				else
				{
					codePosition[ampIndex]+=3;
				}
			}
			else if curAmp[codePosition[ampIndex]]==106
			{
				let inputPosition=curAmp[codePosition[ampIndex]+1] as usize;
				let jumpPosition=curAmp[codePosition[ampIndex]+2] as usize;
				if inputPosition==0
				{
					codePosition[ampIndex]=curAmp[jumpPosition] as usize;
				}
				else
				{
					codePosition[ampIndex]+=3;
				}
			}
			else if curAmp[codePosition[ampIndex]]==1006
			{
				let inputPosition=curAmp[codePosition[ampIndex]+1] as usize;
				let jumpPosition=curAmp[codePosition[ampIndex]+2] as usize;
				if curAmp[inputPosition]==0
				{
					codePosition[ampIndex]=jumpPosition;
				}
				else
				{
					codePosition[ampIndex]+=3;
				}
			}
			else if curAmp[codePosition[ampIndex]]==1106
			{
				let inputPosition=curAmp[codePosition[ampIndex]+1] as usize;
				let jumpPosition=curAmp[codePosition[ampIndex]+2] as usize;
				if inputPosition==0
				{
					codePosition[ampIndex]=jumpPosition;
				}
				else
				{
					codePosition[ampIndex]+=3;
				}
			}
			else if curAmp[codePosition[ampIndex]]==7
			{
				let outputPosition = curAmp[codePosition[ampIndex]+3] as usize;
				let inputPosition1=curAmp[codePosition[ampIndex]+1] as usize;
				let inputPosition2=curAmp[codePosition[ampIndex]+2] as usize;
				if curAmp[inputPosition1]<curAmp[inputPosition2]
				{
					curAmp[outputPosition]=1;
				}
				else
				{
					curAmp[outputPosition]=0;
				}
				codePosition[ampIndex]+=4;
			}
			else if curAmp[codePosition[ampIndex]]==107
			{
				let outputPosition = curAmp[codePosition[ampIndex]+3] as usize;
				let inputPosition1=curAmp[codePosition[ampIndex]+1];
				let inputPosition2=curAmp[codePosition[ampIndex]+2] as usize;
				if inputPosition1<curAmp[inputPosition2]
				{
					curAmp[outputPosition]=1;
				}
				else
				{
					curAmp[outputPosition]=0;
				}
				codePosition[ampIndex]+=4;
			}
			else if curAmp[codePosition[ampIndex]]==1007
			{
				let outputPosition = curAmp[codePosition[ampIndex]+3] as usize;
				let inputPosition1=curAmp[codePosition[ampIndex]+1] as usize;
				let inputPosition2=curAmp[codePosition[ampIndex]+2];
				if curAmp[inputPosition1]<inputPosition2
				{
					curAmp[outputPosition]=1;
				}
				else
				{
					curAmp[outputPosition]=0;
				}
				codePosition[ampIndex]+=4;
			}
			else if curAmp[codePosition[ampIndex]]==1107
			{
				let outputPosition = curAmp[codePosition[ampIndex]+3] as usize;
				let inputPosition1=curAmp[codePosition[ampIndex]+1];
				let inputPosition2=curAmp[codePosition[ampIndex]+2];
				if inputPosition1<inputPosition2
				{
					curAmp[outputPosition]=1;
				}
				else
				{
					curAmp[outputPosition]=0;
				}
				codePosition[ampIndex]+=4;
			}
			else if curAmp[codePosition[ampIndex]]==8
			{
				let outputPosition = curAmp[codePosition[ampIndex]+3] as usize;
				let inputPosition1=curAmp[codePosition[ampIndex]+1] as usize;
				let inputPosition2=curAmp[codePosition[ampIndex]+2] as usize;
				if curAmp[inputPosition1]==curAmp[inputPosition2]
				{
					curAmp[outputPosition]=1;
				}
				else
				{
					curAmp[outputPosition]=0;
				}
				codePosition[ampIndex]+=4;
			}
			else if curAmp[codePosition[ampIndex]]==108
			{
				let outputPosition = curAmp[codePosition[ampIndex]+3] as usize;
				let inputPosition1=curAmp[codePosition[ampIndex]+1];
				let inputPosition2=curAmp[codePosition[ampIndex]+2] as usize;
				if inputPosition1==curAmp[inputPosition2]
				{
					curAmp[outputPosition]=1;
				}
				else
				{
					curAmp[outputPosition]=0;
				}
				codePosition[ampIndex]+=4;
			}
			else if curAmp[codePosition[ampIndex]]==1008
			{
				let outputPosition = curAmp[codePosition[ampIndex]+3] as usize;
				let inputPosition1=curAmp[codePosition[ampIndex]+1] as usize;
				let inputPosition2=curAmp[codePosition[ampIndex]+2];
				if curAmp[inputPosition1]==inputPosition2
				{
					curAmp[outputPosition]=1;
				}
				else
				{
					curAmp[outputPosition]=0;
				}
				codePosition[ampIndex]+=4;
			}
			else if curAmp[codePosition[ampIndex]]==1108
			{
				let outputPosition = curAmp[codePosition[ampIndex]+3] as usize;
				let inputPosition1=curAmp[codePosition[ampIndex]+1];
				let inputPosition2=curAmp[codePosition[ampIndex]+2];
				if inputPosition1==inputPosition2
				{
					curAmp[outputPosition]=1;
				}
				else
				{
					curAmp[outputPosition]=0;
				}
				codePosition[ampIndex]+=4;
			}
			else if curAmp[codePosition[ampIndex]]==99
			{
				break 'outer2;
			}
			else
			{
				println!("Opcode error: {}",curAmp[codePosition[ampIndex]]);
				break 'outer2;
				
			}
		}
		if Output>maxOutput
		{
			maxOutput=Output;
			println!("New max Output:{}",maxOutput);
			println!("Current Best Combination:{:?}",p);
		}
	});
	println!("Second Answer :\n{}",maxOutput);
}
