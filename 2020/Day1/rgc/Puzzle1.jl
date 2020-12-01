er=Int32[]
open("Puzzle1.txt") do f

    timetaken = @time for l in eachline(f)
        push!(er,parse(Int32,l))
    end
end
@show(er)
ans1=0
for i in 1:length(er)
    for j in 1:length(er)
	    if i!=j && er[i]+er[j]==2020
		    @show(er[i]*er[j])
		end
	end
end
for i in 1:length(er)
    for j in 1:length(er)
	    for k in 1:length(er)
	        if i!=j && i!=k && j!=k && er[i]+er[j]+er[k]==2020
		        @show(er[i]*er[j]*er[k])
			end
		end
	end
end
