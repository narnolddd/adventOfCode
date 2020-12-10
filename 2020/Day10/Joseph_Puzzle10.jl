jolt=Int[]
push!(jolt,0)
open("Puzzle10.txt") do f
    timetaken = @time for l in eachline(f)
	     push!(jolt,parse(Int,l))
    end
end
jolt=sort(jolt)
oneDiff=0
threeDiff=1#Your adapter
for i in 1:(length(jolt)-1)
    if jolt[i]==(jolt[i+1]-1)
	    global oneDiff=oneDiff+1
	end
    if jolt[i]==(jolt[i+1]-3)
	    global threeDiff=threeDiff+1
	end
end
ans1=oneDiff*threeDiff	
@show(ans1)
pathCount=1
index=1
while index <=length(jolt)
    seqLen=1
	while jolt[index+1]-jolt[index]==1
	    seqLen+=1
		global index=index+1
		if index==length(jolt)
		    break
		end
	end
	if seqLen==5#Assuming this is the maximum sequence length. May not work for all solutions
	    global pathCount=pathCount*7
	elseif seqLen==4
	    global pathCount=pathCount*4
	elseif seqLen==3
	    global pathCount=pathCount*2
	end
	global index=index+1
end
@show(pathCount)