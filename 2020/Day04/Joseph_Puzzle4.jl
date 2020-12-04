passport=[]
open("Puzzle4.txt") do f
    entry=""
    timetaken = @time for l in eachline(f)
	    if l!=""
		    entry=string(entry,l, " ")
		else
		    push!(passport,entry)
			entry=""
	    end
    end
end
validPassport=[]
ans1=0
for s in passport
    if occursin("byr:",s)&&occursin("iyr:",s)&&occursin("eyr:",s)&&occursin("hgt:",s)&&occursin("hcl:",s)&&occursin("ecl:",s)&&occursin("pid:",s)
	    global ans1 = ans1+1
		push!(validPassport,s)
    end
end
@show(ans1)
ans2=0
for s in validPassport
    test=split(s," ")
	validCounter=0
	for t in test
	    te=split(t,":")
		if te[1]=="byr" && parse(Int32,te[2])<=2002 && parse(Int32,te[2])>=1920
		   validCounter+=1
		elseif te[1]=="iyr" && parse(Int32,te[2])<=2020 && parse(Int32,te[2])>=2010
		   validCounter+=1
		elseif te[1]=="eyr" && parse(Int32,te[2])<=2030 && parse(Int32,te[2])>=2020
		   validCounter+=1 		   
		elseif te[1]=="hgt"
		   if occursin("in",te[2])
		       if parse(Int32,replace(te[2],"in"=>""))>=59 && parse(Int32,replace(te[2],"in"=>""))<=76
			      validCounter+=1
			   end
		   elseif occursin("cm",te[2])
		       if parse(Int32,replace(te[2],"cm"=>""))>=150 && parse(Int32,replace(te[2],"cm"=>""))<=193
			      validCounter+=1
               end
           end			   
		elseif te[1]=="hcl" && (length(te[2])==7)
		   if te[2][1]=='#' && isa(tryparse(Int,te[2][2:7],base=16), Int)
		       validCounter+=1
           end			   
		elseif te[1]=="ecl" && te[2] in ["amb","blu","brn","gry","grn","hzl","oth"]
		   validCounter+=1
		elseif te[1]=="pid" && length(te[2])==9
		   if isa(tryparse(Float64,te[2]), Number)
		       validCounter+=1
		   end
		end
	end
    if validCounter==7
	    global ans2 = ans2+1
    end
end
@show(ans2)