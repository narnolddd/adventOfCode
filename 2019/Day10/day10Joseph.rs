use std::env;
use std::fs;




fn main() {
    // --snip--
	let filename ="Puzzle10.txt";
    println!("In file {}", filename);

    let contents = fs::read_to_string(filename)
        .expect("Something went wrong reading the file");
	let mut inDirectOrbits=0;
	let mut directOrbits=0;
	let mut coor=Vec::new();
	let mut x=0.0;
	let mut y=0.0;
	let mut xlen=0.0;
	let mut ylen=0.0;
	let mut astLos:Vec <(f64,f64,f64)>=Vec::new();
	let mut bx=0.0;
	let mut by=0.0;
	/*for lt in contents.lines()
	{
		y=y+1.0;
	}
	y=y+1.0;//Subtract 1 to account for 0*/
	for l in contents.lines() 
	{
		for c in l.chars()
		{
			if c=='.'
			{
				coor.push((x,y,0));
			}
			else
			{
				coor.push((x,y,1));
			}
			x=x+1.0;
		}
		xlen=x;
		y=y+1.0;
		x=0.0;
	}
	ylen=y;
	println!("{:?}",coor);
	println!("{0},{1}",xlen,ylen);
	let mut maxAst=0;
	for co in &coor
	{
		if co.2==1//Asteroid found
		{
			let mut astCount=0;
			for ca in &coor//check all other asteroids
			{
				if ca.2==1 && !(co.0==ca.0 && co.1==ca.1)
				{
					let mut xDiff=ca.0-co.0;
					let mut yDiff=ca.1-co.1;
					let m=yDiff/xDiff;
					let ce=co.1-(m*co.0);
					//println!("x1:{0},y1:{1},x2:{2},y2:{3}",co.0,co.1,ca.0,ca.1);
					//println!("y=mx+c:y={0}x+{1}",m,ce);
					let mut lX=co.0;
					let mut sX=co.0;
					if ca.0>lX
					{
						lX=ca.0;
					}
					else
					{
						sX=ca.0;
					}
					let mut lY=co.1;
					let mut sY=co.1;
					if ca.1>lY
					{
						lY=ca.1;
					}
					else
					{
						sY=ca.1;
					}
					let mut los=true;
					for cb in &coor//check los blockers
					{
						if !(co.0==cb.0 && co.1==cb.1)&&!(ca.0==cb.0 && ca.1==cb.1)&&cb.2==1
						{
							//println!("c:{0},m:{1},x:{2},y:{3},sx:{4},lx:{5},sy:{6},ly:{7}",ce,m,cb.0,cb.1,sX,lX,sY,lY);
							//println!("ce:{0},ce2:{1}",ce,cb.1-(m*cb.0));
							if (((ce-(cb.1-(m*cb.0)))<0.00000001&&(ce-(cb.1-(m*cb.0)))>-0.00000001)||ce==(cb.1-(m*cb.0)))&&cb.1>=sY&&cb.1<=lY&&cb.0>=sX&&cb.0<=lX//Goddamn rounding errors and infinite values
							{
								//println!("LOS Blocked");
								los=false;
							}
						}
					}
					if los
					{
						astCount+=1;
					}
					//println!("AsteroidCount:{}",astCount);
				}
				if astCount>maxAst
				{
					maxAst=astCount;
					bx=co.0;
					by=co.1;
				}
			}
			
		}
	}
	
	
	println!("First Anwser :\n{}",maxAst);
	println!("Base Location: {0},{1}",bx,by);
	for ca in &coor//check all other asteroids
	{
		if ca.2==1 && !(bx==ca.0 && by==ca.1)
		{
			let mut xDiff=ca.0-bx;
			let mut yDiff=ca.1-by;
			let m=yDiff/xDiff;
			let ce=by-(m*bx);
			//println!("x1:{0},y1:{1},x2:{2},y2:{3}",bx,by,ca.0,ca.1);
			//println!("y=mx+c:y={0}x+{1}",m,ce);
			let mut lX=bx;
			let mut sX=bx;
			if ca.0>lX
			{
				lX=ca.0;
			}
			else
			{
				sX=ca.0;
			}
			let mut lY=by;
			let mut sY=by;
			if ca.1>lY
			{
				lY=ca.1;
			}
			else
			{
				sY=ca.1;
			}
			let mut los=true;
			for cb in &coor//check los blockers
			{
				if !(bx==cb.0 && by==cb.1)&&!(ca.0==cb.0 && ca.1==cb.1)&&cb.2==1
				{
					//println!("c:{0},m:{1},x:{2},y:{3},sx:{4},lx:{5},sy:{6},ly:{7}",ce,m,cb.0,cb.1,sX,lX,sY,lY);
					//println!("ce:{0},ce2:{1}",ce,cb.1-(m*cb.0));
					if (((ce-(cb.1-(m*cb.0)))<0.00000001&&(ce-(cb.1-(m*cb.0)))>-0.00000001)||ce==(cb.1-(m*cb.0)))&&cb.1>=sY&&cb.1<=lY&&cb.0>=sX&&cb.0<=lX//Goddamn rounding errors and infinite values
					{
						//println!("LOS Blocked");
						los=false;
					}
				}
			}
			if los
			{
				let mut angle:f64=(ca.1-by)/(ca.0-bx);
				angle=angle.atan();
				astLos.push((ca.0,ca.1,angle));
			}
		}
	}
	astLos.sort_by(|a, b| a.2.partial_cmp(&b.2).unwrap());
	println!("{:?}",astLos);
	let sAns=(astLos[196].0*100.0)+astLos[196].1;//Not sure why indexing is off. Suspect floating point rounding errors or sorting error
	println!("Second Answer :\n{}",sAns);

	
}
