use std::env;
use std::fs;

fn orbitCalculator(vg: Vec<&str>, ino:i32, cn:&str,tino:&mut i32,tdo:&mut i32)
{
	for ti in (0..vg.len()).step_by(2)
	{
		if vg[ti]==cn
		{
			let newVG=vg.clone();
			orbitCalculator(newVG,ino+1,vg[ti+1],tino,tdo);
		}	
	}
	*tino+=ino-1;
	*tdo+=1;
}




fn main() {
    // --snip--
	let filename ="Puzzle6.txt";
    println!("In file {}", filename);

    let contents = fs::read_to_string(filename)
        .expect("Something went wrong reading the file");
	let mut inDirectOrbits=0;
	let mut directOrbits=0;
	let mut ys=Vec::new();
	for l in contents.lines() 
	{
		let stringSplit:Vec<&str> = l.split(')').collect();
		ys.push(stringSplit[0]);
		ys.push(stringSplit[1]);
	}
	let mut rIndex=0;
	let mut ys2=ys.clone();
	for i in 0..ys.len()
	{
		if ys[i]=="COM"
		{
			rIndex=i+1;
			break;
		}
	}
	let child=ys[rIndex];
	orbitCalculator(ys,1,&child,&mut inDirectOrbits,&mut directOrbits);
	println!("Indirect Orbits:{}",inDirectOrbits);
	println!("Direct Orbits:{}",directOrbits);
	println!("First Anwser :\n{}",inDirectOrbits+directOrbits);
	let mut visitedWorlds:Vec<(&str,i32)>=Vec::new();
	let mut finalPath=0;
	for i in 0..ys2.len()
	{
		if ys2[i]=="YOU"
		{
			rIndex=i-1;
			visitedWorlds.push((ys2[rIndex],0));
			break;
		}
	}
	let mut wIndex=0;
	'SantaNotFound: loop
	{
			let curW=visitedWorlds[wIndex].0;
			let pathLen=visitedWorlds[wIndex].1;
			for y in 0..ys2.len()
			{
				if ys2[y]==curW
				{
					if y%2==0
					{
						let mut alreadyAdded=false;
						for v in &visitedWorlds
						{
							if v.0==ys2[y+1]
							{
								alreadyAdded=true;
							}
						}
						if !alreadyAdded
						{
							visitedWorlds.push((ys2[y+1],pathLen+1));
							if ys2[y+1]=="SAN"
							{
								finalPath=pathLen;
								break 'SantaNotFound;
							}
						}
					}
					else
					{
						let mut alreadyAdded=false;
						for v in &visitedWorlds
						{
							if v.0==ys2[y-1]
							{
								alreadyAdded=true;
							}
						}
						if !alreadyAdded
						{
							visitedWorlds.push((ys2[y-1],pathLen+1));
							if ys2[y-1]=="SAN"
							{
								finalPath=pathLen;
								break 'SantaNotFound;
							}
						}
						if ys2[y-1]=="SAN"
						{
							finalPath=pathLen;
							break 'SantaNotFound;
						}
					}
				}
			}
			wIndex+=1;		
	}
	println!("Second Answer :\n{}",finalPath);

	
}
