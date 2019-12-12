
use std::env;
use std::fs;
use std::cmp::{max, min};
fn gcd(a: usize, b: usize) -> usize {
    match ((a, b), (a & 1, b & 1)) {
        ((x, y), _) if x == y => y,
        ((0, x), _) | ((x, 0), _) => x,
        ((x, y), (0, 1)) | ((y, x), (1, 0)) => gcd(x >> 1, y),
        ((x, y), (0, 0)) => gcd(x >> 1, y >> 1) << 1,
        ((x, y), (1, 1)) => {
            let (x, y) = (min(x, y), max(x, y));
            gcd((y - x) >> 1, x)
        }
        _ => unreachable!(),
    }
}
 
fn lcm(a: usize, b: usize) -> usize {
	println!("a:{0},b:{1}",a,b);
    a * b / gcd(a, b)
}



fn main() {
    // --snip--
	//let filename ="Puzzle12.txt";
    //println!("In file {}", filename);

    /*let contents = fs::read_to_string(filename)
        .expect("Something went wrong reading the file");*/
	let mut moonPos: Vec<(i32,i32,i32)>=Vec::new();
	//Input hardcoded as parsing looked like a bit of a pain. Fix later
	/*<x=6, y=10, z=10>
	<x=-9, y=3, z=17>
	<x=9, y=-4, z=14>
	<x=4, y=14, z=4>*/
	moonPos.push((6,10,10));
	moonPos.push((-9,3,17));
	moonPos.push((9,-4,14));
	moonPos.push((4,14,4));
	let mut moonVec: Vec<(i32,i32,i32)>=Vec::new();
	moonVec.push((0,0,0));
	moonVec.push((0,0,0));
	moonVec.push((0,0,0));
	moonVec.push((0,0,0));

	for x in 0..1000
	{
		for v in 0..4
		{
			for p in 0..4
			{
				if v!=p
				{
					if moonPos[v].0<moonPos[p].0
					{
						moonVec[v].0=moonVec[v].0+1;
					}
					else if moonPos[v].0>moonPos[p].0
					{
						moonVec[v].0=moonVec[v].0-1;
					}
					if moonPos[v].1<moonPos[p].1
					{
						moonVec[v].1=moonVec[v].1+1;
					}
					else if moonPos[v].1>moonPos[p].1
					{
						moonVec[v].1=moonVec[v].1-1;
					}
					if moonPos[v].2<moonPos[p].2
					{
						moonVec[v].2=moonVec[v].2+1;
					}
					else if moonPos[v].2>moonPos[p].2
					{
						moonVec[v].2=moonVec[v].2-1;
					}
				}
			}
		}
		for v in 0..4
		{
			moonPos[v].0+=moonVec[v].0;
			moonPos[v].1+=moonVec[v].1;
			moonPos[v].2+=moonVec[v].2;
		}
	}
	let mut tEng=0;
	for v in 0..4
	{
		tEng=tEng+(moonPos[v].0.abs()+moonPos[v].1.abs()+moonPos[v].2.abs())*(moonVec[v].0.abs()+moonVec[v].1.abs()+moonVec[v].2.abs());
	}

	moonPos.clear();
	moonVec.clear();
	
	println!("First Anwser :\n{}",tEng);
	moonPos.push((6,10,10));
	moonPos.push((-9,3,17));
	moonPos.push((9,-4,14));
	moonPos.push((4,14,4));
	moonVec.push((0,0,0));
	moonVec.push((0,0,0));
	moonVec.push((0,0,0));
	moonVec.push((0,0,0));
	let mut moonStateX: Vec<(i32,i32,i32,i32,i32,i32,i32,i32)>=Vec::new();
	let mut moonStateY: Vec<(i32,i32,i32,i32,i32,i32,i32,i32)>=Vec::new();
	let mut moonStateZ: Vec<(i32,i32,i32,i32,i32,i32,i32,i32)>=Vec::new();
	moonStateX.push((moonPos[0].0,moonPos[1].0,moonPos[2].0,moonPos[3].0,moonVec[0].0,moonVec[1].0,moonVec[2].0,moonVec[3].0));
	moonStateY.push((moonPos[0].1,moonPos[1].1,moonPos[2].1,moonPos[3].1,moonVec[0].1,moonVec[1].1,moonVec[2].1,moonVec[3].1));
	moonStateZ.push((moonPos[0].2,moonPos[1].2,moonPos[2].2,moonPos[3].2,moonVec[0].2,moonVec[1].2,moonVec[2].2,moonVec[3].2));
	let mut xLoop=false;
	let mut xStep:usize=1;//One for first step
	let mut yLoop=false;
	let mut yStep:usize=1;
	let mut zLoop=false;
	let mut zStep:usize=1;
	let mut step=0;
	'outer1: loop
	{
		for v in 0..4
		{
			for p in 0..4
			{
				if v!=p
				{
					if moonPos[v].0<moonPos[p].0
					{
						moonVec[v].0=moonVec[v].0+1;
					}
					else if moonPos[v].0>moonPos[p].0
					{
						moonVec[v].0=moonVec[v].0-1;
					}
					if moonPos[v].1<moonPos[p].1
					{
						moonVec[v].1=moonVec[v].1+1;
					}
					else if moonPos[v].1>moonPos[p].1
					{
						moonVec[v].1=moonVec[v].1-1;
					}
					if moonPos[v].2<moonPos[p].2
					{
						moonVec[v].2=moonVec[v].2+1;
					}
					else if moonPos[v].2>moonPos[p].2
					{
						moonVec[v].2=moonVec[v].2-1;
					}
				}
			}
		}
		for v in 0..4
		{
			moonPos[v].0+=moonVec[v].0;
			moonPos[v].1+=moonVec[v].1;
			moonPos[v].2+=moonVec[v].2;
		}
		if !xLoop
		{
			if moonStateX.contains(&(moonPos[0].0,moonPos[1].0,moonPos[2].0,moonPos[3].0,moonVec[0].0,moonVec[1].0,moonVec[2].0,moonVec[3].0))
			{
				xLoop=true;
				println!("X Loop Detected at {}",xStep); 
				//println!("{:?}",moonStateX);
			}
			else
			{
				moonStateX.push((moonPos[0].0,moonPos[1].0,moonPos[2].0,moonPos[3].0,moonVec[0].0,moonVec[1].0,moonVec[2].0,moonVec[3].0));
				xStep+=1;
			}
		}
		if !yLoop
		{
			if moonStateY.contains(&(moonPos[0].1,moonPos[1].1,moonPos[2].1,moonPos[3].1,moonVec[0].1,moonVec[1].1,moonVec[2].1,moonVec[3].1))
			{
				yLoop=true;
				println!("Y Loop Detected at {}",yStep); 
				//println!("{:?}",moonStateY);
			}
			else
			{
				moonStateY.push((moonPos[0].1,moonPos[1].1,moonPos[2].1,moonPos[3].1,moonVec[0].1,moonVec[1].1,moonVec[2].1,moonVec[3].1));
				yStep+=1;
			}
		}
		if !zLoop
		{
			if moonStateZ.contains(&(moonPos[0].2,moonPos[1].2,moonPos[2].2,moonPos[3].2,moonVec[0].2,moonVec[1].2,moonVec[2].2,moonVec[3].2))
			{
				zLoop=true;
				println!("Z Loop Detected at {}",zStep);
				//println!("{:?}",moonStateZ);			
			}
			else
			{
				moonStateZ.push((moonPos[0].2,moonPos[1].2,moonPos[2].2,moonPos[3].2,moonVec[0].2,moonVec[1].2,moonVec[2].2,moonVec[3].2));
				zStep+=1;
			}
		}
		if xLoop&&yLoop&&zLoop
		{
			break 'outer1;
		}
		step+=1;
		if step%10000==0
		{
			println!("Step:{}",step);
		}
	}
	let sAns=lcm(xStep,yStep);
	let sAnsF=lcm(sAns,zStep);
	println!("Second Answer :\n{}",sAnsF);

	
}
