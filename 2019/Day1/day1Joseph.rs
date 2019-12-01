use std::env;
use std::fs;

fn main() {
    // --snip--
	let filename ="Puzzle1.txt";
    println!("In file {}", filename);

    let contents = fs::read_to_string(filename)
        .expect("Something went wrong reading the file");
	let mut fuelSum =0;
	for l in contents.lines() 
	{ 
		println!("{}",l);
		fuelSum+=(l.parse::<i32>().unwrap()/3)-2;

	}

    println!("First Answer:\n{}", fuelSum);
	let mut totalFuel=0;
	for l in contents.lines() 
	{ 
		//println!("{}",l);
		let mut originalFuel=(l.parse::<i32>().unwrap()/3)-2;
		'outer: loop
		{
			totalFuel+=originalFuel;
			originalFuel=(originalFuel/3)-2;
			if originalFuel<3
			{
				if originalFuel>0
				{
					totalFuel+=originalFuel;
				}
				break 'outer;
			}
			println!("Total Fuel {}",totalFuel);
		}
		println!("Total Fuel {}",totalFuel);
	}
	println!("Second Answer:\n{}", totalFuel);
	
}
