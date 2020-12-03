map=[]
open("Puzzle3.txt") do f
    timetaken = @time for l in eachline(f)
	    tempMap=Char[]
	    for i in 1:length(l)
	       push!(tempMap,l[i])
		end
		push!(map,tempMap)
    end
end
ans1=0
x=4
y=2
while y<=length(map)
    if x > length(map[1])
	    x = x-length(map[1])
    end
	if map[y][x]=='#'
	    global ans1=ans1+1
	end
	global x = x+3
	global y = y +1
end
@show(ans1)
ans2=0
step=[[1,1],[3,1],[5,1],[7,1],[1,2]]
for j in 1:length(step)
    global x = 1+step[j][1]
	global y = 1+step[j][2]
	global ans1=0
    while y<=length(map)
        if x > length(map[1])
	        x = x-length(map[1])
        end
	    if map[y][x]=='#'
	        global ans1=ans1+1
	    end
	    global x = x+step[j][1]
	    global y = y +step[j][2]
	end
	if ans2==0
	    global ans2=ans1
	else
	    global ans2=ans2*ans1
	end
end
@show(ans2)
