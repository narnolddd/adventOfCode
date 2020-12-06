questions=String[]
numPeople=[]
open("Puzzle6.txt") do f
    entry=""
	people=0
    timetaken = @time for l in eachline(f)
	    if l!=""
		    entry=string(entry,l, " ")
			people+=1
		else
		    push!(questions,entry)
			push!(numPeople,people)
			people=0
			entry=""
	    end
    end
end
ans1=0
ans2=0
index=1
for q in questions
    lCount=0
    uniq=unique(q)
	for u in uniq
	    if isletter(u)
		   lCount+=1
		   if count(a->(a==u),q)==numPeople[index]
		       global ans2=ans2+1
		   end
		end
	end
	global ans1=ans1+lCount
	global index=index+1
end
@show(ans1)
@show(ans2)
