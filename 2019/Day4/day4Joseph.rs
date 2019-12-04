use std::env;
use std::fs;

fn main() {
    // --snip--

	
	let mut passwordCounter=0;
	let mut possibleSecondaryPasswords=Vec::new();
	for x in 156218..652527
	{
		let mut i =x as u32;
		let mut div =100000;
		let mut digits = Vec::new();
		let mut currentDigit=i/div;
		let mut previousDigit=currentDigit;
		i=i%div;
		div=div/10;
		digits.push(currentDigit);
		let mut doubleDigit=false;
		while div !=0
		{
			currentDigit=i/div;
			if currentDigit<previousDigit
			{
				break;
			}
			i=i%div;
			div=div/10;
			if digits.contains(&currentDigit)
			{
				doubleDigit=true;
			}
			digits.push(currentDigit);
			previousDigit=currentDigit;
		}
			
		if div==0 && doubleDigit
		{
			passwordCounter+=1;
			possibleSecondaryPasswords.push(x);
		}
	}

	println!("First Anwser :\n{}",passwordCounter);
	
	let mut threeDigitCounter=0;
	for p in possibleSecondaryPasswords
	{
		let mut i =p as u32;
		let mut div =100000;
		let mut currentDigit=i/div;
		let mut sequenceLength=1;
		let mut previousDigit=currentDigit;
		let mut sequences=Vec::new();
		i=i%div;
		div=div/10;
		while div !=0
		{
			currentDigit=i/div;
			if currentDigit!=previousDigit
			{
				sequences.push((previousDigit,sequenceLength));
				sequenceLength=1;
			}
			else
			{
				sequenceLength+=1;
			}
			i=i%div;
			div=div/10;
			previousDigit=currentDigit;
		}
		sequences.push((currentDigit,sequenceLength));
		let mut doubleDigitsOnly=false;
		for d in sequences
		{
			if d.1==2
			{
				doubleDigitsOnly=true;
			}
		}
		if !doubleDigitsOnly
		{
			threeDigitCounter+=1;
		}


	}
	let finalPasswords=passwordCounter-threeDigitCounter;
	println!("Second Anwser :\n{}",finalPasswords);
}	
