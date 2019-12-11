use std::env;
use std::fs;

fn main() {
    // --snip--
	let filename ="Puzzle11.txt";
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
	let mut x=0;
	let mut y=0;
	let mut pSq=Vec::new();
	let mut pSqN=Vec::new();
	let mut index=0;
	let mut xDir=0;
	let mut yDir=1;
	let mut indexM=0;
	for s in sSplit
	{
		if s.parse::<i64>().is_ok()
		{
			opCodes.push(s.parse::<i64>().unwrap())
		}
	}
	for x in 0..1000//Create additional opCode memory
	{
		opCodes.push(0);
	}
	'outer1: loop
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
			let mut input = 0;//Input defined in problem statement
			if pSq.contains(&(x,y))
			{
				input=1;
			}
			let outputPosition = opCodes[index+1] as usize;
			opCodes[outputPosition]=input;
			//println!("Input:{}",input);
			index+=2;
		}
		else if opCodes[index]==4
		{
			let outputPosition = opCodes[index+1] as usize;
			//println!("Output:{}",opCodes[outputPosition]);
			//println!("IndexM:{}",indexM);
			firstOutput=opCodes[outputPosition];
			if indexM%2==0
			{
				if !pSqN.contains(&(x,y))
				{
					pSqN.push((x,y));
				}
				if firstOutput==1
				{
					if !pSq.contains(&(x,y))
					{
						pSq.push((x,y));
					}
				}
				else
				{
					if pSq.contains(&(x,y))
					{
						//println!("(x,y):({0},{1})",x,y);
						//println!("{:?}",pSq);
						let mut indexT: usize = 0;
						let mut indexR: usize = 0;
						for p in &pSq
						{
							if p.0==x &&p.1==y
							{
								indexR=indexT
							}
							indexT+=1;
						}
						pSq.remove(indexR);
						//println!("{:?}",pSq);
					}
				}
			}
			else
			{
				//println!("{0},{1},{2},{3},{4}",firstOutput,x,y,xDir,yDir);
				if firstOutput ==1
				{
					if yDir==1
					{
						xDir=1;
						yDir=0;
					}
					else if xDir==1
					{
						yDir=-1;
						xDir=0;
					}
					else if yDir==-1
					{
						xDir=-1;
						yDir=0;
					}
					else if xDir==-1
					{
						xDir=0;
						yDir=1;
					}
				}
				else
				{
					if yDir==1
					{
						xDir=-1;
						yDir=0;
					}
					else if xDir==1
					{
						yDir=1;
						xDir=0;
					}
					else if yDir==-1
					{
						xDir=1;
						yDir=0;
					}
					else if xDir==-1
					{
						xDir=0;
						yDir=-1;
					}
				}
				x+=xDir;
				y+=yDir;
				//println!("curr_pos:[{0}, {1}]",x,y);
			}
			indexM+=1;	
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
		else if opCodes[index]==104
		{
			let outputPosition = opCodes[index+1];
			//println!("Output:{}",outputPosition);
			firstOutput=outputPosition;
			if indexM%2==0
			{
				if !pSqN.contains(&(x,y))
				{
					pSqN.push((x,y));
				}
				if firstOutput==1
				{
					if !pSq.contains(&(x,y))
					{
						pSq.push((x,y));
					}
					else
					{
						if pSq.contains(&(x,y))
						{
							let mut indexT: usize = 0;
							let mut indexR: usize = 0;
							for p in &pSq
							{
								if p.0==x &&p.1==y
								{
									indexR=indexT
								}
								indexT+=1;
							}
							pSq.remove(indexR);
						}
					}
				}
			}
			else
			{
				//println!("{0},{1},{2},{3},{4}",firstOutput,x,y,xDir,yDir);
				if firstOutput ==1
				{
					if yDir==1
					{
						xDir=1;
						yDir=0;
					}
					else if xDir==1
					{
						yDir=-1;
						xDir=0;
					}
					else if yDir==-1
					{
						xDir=-1;
						yDir=0;
					}
					else if xDir==-1
					{
						xDir=0;
						yDir=1;
					}
				}
				else
				{
					if yDir==1
					{
						xDir=-1;
						yDir=0;
					}
					else if xDir==1
					{
						yDir=1;
						xDir=0;
					}
					else if yDir==-1
					{
						xDir=1;
						yDir=0;
					}
					else if xDir==-1
					{
						xDir=0;
						yDir=-1;
					}
				}
				x+=xDir;
				y+=yDir;
				//println!("curr_pos:[{0}, {1}]",x,y);
			}
			indexM+=1;
			index+=2;
		}
		else if opCodes[index]==204
		{
			let outputPosition = (opCodes[index+1]+relativeBase) as usize;
			//println!("Output:{}",opCodes[outputPosition]);
			firstOutput=opCodes[outputPosition];
			if indexM%2==0
			{
				if !pSqN.contains(&(x,y))
				{
					pSqN.push((x,y));
				}
				if firstOutput==1
				{
					if !pSq.contains(&(x,y))
					{
						pSq.push((x,y));
					}
				}
				else
				{
					if pSq.contains(&(x,y))
					{
						let mut indexT: usize = 0;
						let mut indexR: usize = 0;
						for p in &pSq
						{
							if p.0==x &&p.1==y
							{
								indexR=indexT
							}
							indexT+=1;
						}
						pSq.remove(indexR);
					}
				}
			}
			else
			{
				//println!("{0},{1},{2},{3},{4}",firstOutput,x,y,xDir,yDir);
				if firstOutput ==1
				{
					if yDir==1
					{
						xDir=1;
						yDir=0;
					}
					else if x==1
					{
						yDir=-1;
						xDir=0;
					}
					else if yDir==-1
					{
						xDir=-1;
						yDir=0;
					}
					else if xDir==-1
					{
						xDir=0;
						yDir=1;
					}
				}
				else
				{
					if yDir==1
					{
						xDir=-1;
						yDir=0;
					}
					else if x==1
					{
						yDir=1;
						xDir=0;
					}
					else if yDir==-1
					{
						xDir=1;
						yDir=0;
					}
					else if xDir==-1
					{
						xDir=0;
						yDir=-1;
					}
				}
				x+=xDir;
				y+=yDir;
				//println!("curr_pos:[{0}, {1}]",x,y);
			}
			indexM+=1;
			index+=2;
		}
		else if opCodes[index]==203
		{
			let mut input = 0;//Input defined in problem statement
			if pSq.contains(&(x,y))
			{
				input=1;
			}
			let outputPosition = (relativeBase+opCodes[index+1]) as usize;
			opCodes[outputPosition]=input;
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
			break 'outer1;
		}
		else
		{
			println!("Opcode error: {}",opCodes[index]);
			break 'outer1;
			
		}
	}

	//println!("{:?}",pSq);
	println!("First Answer :\n{}",pSqN.len());
	opCodes.clear();
	pSq.clear();
	pSq.push((0,0));
	let ssSplit = contents.split(',');
	relativeBase=0;
	index=0;
	x=0;
	y=0;
	xDir=0;
	yDir=1;
	indexM=0;
	for s in ssSplit
	{
		if s.parse::<i64>().is_ok()
		{
			opCodes.push(s.parse::<i64>().unwrap())
		}
	}
	for x in 0..1000//Create additional opCode memory
	{
		opCodes.push(0);
	}
	'outer2: loop
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
			let mut input = 0;//Input defined in problem statement
			if pSq.contains(&(x,y))
			{
				input=1;
			}
			let outputPosition = opCodes[index+1] as usize;
			opCodes[outputPosition]=input;
			//println!("Input:{}",input);
			index+=2;
		}
		else if opCodes[index]==4
		{
			let outputPosition = opCodes[index+1] as usize;
			//println!("Output:{}",opCodes[outputPosition]);
			//println!("IndexM:{}",indexM);
			firstOutput=opCodes[outputPosition];
			if indexM%2==0
			{
				if !pSqN.contains(&(x,y))
				{
					pSqN.push((x,y));
				}
				if firstOutput==1
				{
					if !pSq.contains(&(x,y))
					{
						pSq.push((x,y));
					}
				}
				else
				{
					if pSq.contains(&(x,y))
					{
						//println!("(x,y):({0},{1})",x,y);
						//println!("{:?}",pSq);
						let mut indexT: usize = 0;
						let mut indexR: usize = 0;
						for p in &pSq
						{
							if p.0==x &&p.1==y
							{
								indexR=indexT
							}
							indexT+=1;
						}
						pSq.remove(indexR);
						//println!("{:?}",pSq);
					}
				}
			}
			else
			{
				//println!("{0},{1},{2},{3},{4}",firstOutput,x,y,xDir,yDir);
				if firstOutput ==1
				{
					if yDir==1
					{
						xDir=1;
						yDir=0;
					}
					else if xDir==1
					{
						yDir=-1;
						xDir=0;
					}
					else if yDir==-1
					{
						xDir=-1;
						yDir=0;
					}
					else if xDir==-1
					{
						xDir=0;
						yDir=1;
					}
				}
				else
				{
					if yDir==1
					{
						xDir=-1;
						yDir=0;
					}
					else if xDir==1
					{
						yDir=1;
						xDir=0;
					}
					else if yDir==-1
					{
						xDir=1;
						yDir=0;
					}
					else if xDir==-1
					{
						xDir=0;
						yDir=-1;
					}
				}
				x+=xDir;
				y+=yDir;
				//println!("curr_pos:[{0}, {1}]",x,y);
			}
			indexM+=1;	
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
		else if opCodes[index]==104
		{
			let outputPosition = opCodes[index+1];
			//println!("Output:{}",outputPosition);
			firstOutput=outputPosition;
			if indexM%2==0
			{
				if !pSqN.contains(&(x,y))
				{
					pSqN.push((x,y));
				}
				if firstOutput==1
				{
					if !pSq.contains(&(x,y))
					{
						pSq.push((x,y));
					}
					else
					{
						if pSq.contains(&(x,y))
						{
							let mut indexT: usize = 0;
							let mut indexR: usize = 0;
							for p in &pSq
							{
								if p.0==x &&p.1==y
								{
									indexR=indexT
								}
								indexT+=1;
							}
							pSq.remove(indexR);
						}
					}
				}
			}
			else
			{
				//println!("{0},{1},{2},{3},{4}",firstOutput,x,y,xDir,yDir);
				if firstOutput ==1
				{
					if yDir==1
					{
						xDir=1;
						yDir=0;
					}
					else if xDir==1
					{
						yDir=-1;
						xDir=0;
					}
					else if yDir==-1
					{
						xDir=-1;
						yDir=0;
					}
					else if xDir==-1
					{
						xDir=0;
						yDir=1;
					}
				}
				else
				{
					if yDir==1
					{
						xDir=-1;
						yDir=0;
					}
					else if xDir==1
					{
						yDir=1;
						xDir=0;
					}
					else if yDir==-1
					{
						xDir=1;
						yDir=0;
					}
					else if xDir==-1
					{
						xDir=0;
						yDir=-1;
					}
				}
				x+=xDir;
				y+=yDir;
				//println!("curr_pos:[{0}, {1}]",x,y);
			}
			indexM+=1;
			index+=2;
		}
		else if opCodes[index]==204
		{
			let outputPosition = (opCodes[index+1]+relativeBase) as usize;
			//println!("Output:{}",opCodes[outputPosition]);
			firstOutput=opCodes[outputPosition];
			if indexM%2==0
			{
				if !pSqN.contains(&(x,y))
				{
					pSqN.push((x,y));
				}
				if firstOutput==1
				{
					if !pSq.contains(&(x,y))
					{
						pSq.push((x,y));
					}
				}
				else
				{
					if pSq.contains(&(x,y))
					{
						let mut indexT: usize = 0;
						let mut indexR: usize = 0;
						for p in &pSq
						{
							if p.0==x &&p.1==y
							{
								indexR=indexT
							}
							indexT+=1;
						}
						pSq.remove(indexR);
					}
				}
			}
			else
			{
				//println!("{0},{1},{2},{3},{4}",firstOutput,x,y,xDir,yDir);
				if firstOutput ==1
				{
					if yDir==1
					{
						xDir=1;
						yDir=0;
					}
					else if x==1
					{
						yDir=-1;
						xDir=0;
					}
					else if yDir==-1
					{
						xDir=-1;
						yDir=0;
					}
					else if xDir==-1
					{
						xDir=0;
						yDir=1;
					}
				}
				else
				{
					if yDir==1
					{
						xDir=-1;
						yDir=0;
					}
					else if x==1
					{
						yDir=1;
						xDir=0;
					}
					else if yDir==-1
					{
						xDir=1;
						yDir=0;
					}
					else if xDir==-1
					{
						xDir=0;
						yDir=-1;
					}
				}
				x+=xDir;
				y+=yDir;
				//println!("curr_pos:[{0}, {1}]",x,y);
			}
			indexM+=1;
			index+=2;
		}
		else if opCodes[index]==203
		{
			let mut input = 0;//Input defined in problem statement
			if pSq.contains(&(x,y))
			{
				input=1;
			}
			let outputPosition = (relativeBase+opCodes[index+1]) as usize;
			opCodes[outputPosition]=input;
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
			break 'outer2;
		}
		else
		{
			println!("Opcode error: {}",opCodes[index]);
			break 'outer2;
			
		}
	}
	//println!("{:?}",pSq);
	let mut minX=0;
	let mut maxX=0;
	let mut minY=0;
	let mut maxY=0;
	for p in &pSq
	{
		if p.0<minX
		{
			minX=p.0;
		}
		if p.0>maxX
		{
			maxX=p.0;
		}
		if -p.1<minY//This is mirrored for some reason. Need to figure out why
		{
			minY=-p.1;
		}
		if -p.1>maxY
		{
			maxY=-p.1;
		}
	}
	//println!("MinX:{0},MaxX:{1},MinY:{2},MaxY:{3}",minX,maxX,minY,maxY);
	println!("Second Answer");
	for ty in minY-1..maxY+1
	{
		for tx in minX-1..maxX+1
		{
			if pSq.contains(&(tx,-ty))
			{
				print!("1");
			}
			else
			{
				print!(" ");
			}
		}
		println!("");
	}
	
}
