data=Int[]
open("Puzzle9.txt") do f
    timetaken = @time for l in eachline(f)
	     push!(data,parse(Int,l))
    end
end
instructionsUtilized=[]
ans1=0
for i in 26:length(data)
    errorDetected=true
    for j in (i-25):i-1
	    for k in (i-25):i-1
		     if j!=k && (data[j]+data[k])==data[i]
			     errorDetected=false
		      end
	    end
	end
	if errorDetected
	    global ans1=data[i]
	end 
end	
@show(ans1)
deleteat!(data,findall(x->x>=ans1,data))
global ans2=0
for i in 2:length(data)
    for j in 1:(length(data)-i)
	    check=Int[]
	    for k in 1:i
	        push!(check,data[j+k])
		end
		if sum(check)==ans1
		   global ans2=minimum(check)+maximum(check)
		end
	end
end
@show(ans2)
