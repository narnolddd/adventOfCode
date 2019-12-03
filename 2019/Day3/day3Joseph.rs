use std::env;
use std::fs;

fn main() {
    // --snip--
	let filename ="Puzzle3.txt";
    println!("In file {}", filename);

    let contents = fs::read_to_string(filename)
        .expect("Something went wrong reading the file");
	
	let mut grid=Vec::new();
	let mut overList=Vec::new();
	let mut stepCount=Vec::new();
	let mut wireOne=true;
	for l in contents.lines() 
	{
		let mut x =0;
		let mut y =0;
		let mut step=0;
		let stringSplit = l.split(',');
		for s in stringSplit
		{
			println!("{}",s);
			if s.chars().next().unwrap() =='R'
			{
				//println!("Plus detected");
				if s[1..].parse::<i32>().is_err()
				{
					println!("Failed to parse");
				}
				else
				{
					let distance=s[1..].parse::<i32>().unwrap();
					for i in x..x+distance
					{
						if wireOne==true
						{
							grid.push((i,y,step));
						}
						else 
						{
							for g in &grid
							{
								if g.0==i && g.1==y && i!=0
								{
									overList.push((i,y));
									let totalSteps=g.2+step;
									stepCount.push(totalSteps);
								}
							}
						}
						step+=1;
					}
					x+=distance;

				}
				
				
			}
			if s.chars().next().unwrap() =='L'
			{
				//println!("Plus detected");
				if s[1..].parse::<i32>().is_err()
				{
					println!("Failed to parse");
				}
				else
				{
					let distance=s[1..].parse::<i32>().unwrap();
					let finalStep=step+distance;
					let mut count=0;
					for i in x-distance..x
					{

						if wireOne==true
						{
							grid.push((i,y,(finalStep-count)));
						}
						else 
						{
							for g in &grid
							{
								if g.0==i && g.1==y && i!=0
								{
									overList.push((i,y));
									let totalSteps=g.2+(finalStep-count);
									stepCount.push(totalSteps);
								}
							}
						}
						step+=1;
						count+=1;
					}
					x-=distance;
				}
			}
			if s.chars().next().unwrap() =='U'
			{
				//println!("Plus detected");
				if s[1..].parse::<i32>().is_err()
				{
					println!("Failed to parse");
				}
				else
				{
					let distance=s[1..].parse::<i32>().unwrap();
					for i in y..y+distance
					{
						if wireOne==true
						{
							grid.push((x,i,step));
							
						}
						else 
						{
							for g in &grid
							{
								if g.0==x && g.1==i && i!=0
								{
									overList.push((x,i));
									let totalSteps=g.2+step;
									stepCount.push(totalSteps);
								}
							}
						}
						step+=1;
					}
					y+=distance;
				}
			}
			if s.chars().next().unwrap() =='D'
			{
				//println!("Plus detected");
				if s[1..].parse::<i32>().is_err()
				{
					println!("Failed to parse");
				}
				else
				{
					let distance=s[1..].parse::<i32>().unwrap();
					let finalStep=step+distance;
					let mut count=0;
					for i in y-distance..y
					{
						if wireOne==true
						{
							grid.push((x,i,(finalStep-count)));
							
						}
						else 
						{
							for g in &grid
							{
								if g.0==x && g.1==i && i!=0
								{
									overList.push((x,i));
									let totalSteps=g.2+(finalStep-count);
									stepCount.push(totalSteps);
								}
							}
						}
						step+=1;
						count+=1;
					}
					y-=distance;
				}
			}
			println!("{0},{1}",x,y);		
		}
		wireOne=false;
		//println!("{:?}",grid);
		println!("{:?}", overList);
	}
	println!("{:?}", overList);
	let mut minDistance=100000;
	for j in overList
	{

		if (j.0.abs()+j.1.abs())<minDistance && (j.0.abs()+j.1.abs())!=0
		{
			minDistance=j.0.abs()+j.1.abs();
		}

	}

	println!("First Anwser :\n{}",minDistance);
	let mut minStep=100000;
	for k in stepCount
	{
		if k<minStep && k!=0
		{
			minStep=k;
		}
	}
	println!("Second Answer :\n{}",minStep);

	
}
