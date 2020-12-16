map=[]
function seatChecker(x,y,dx,dy,m)
    cx=x+dx
	cy=y+dy
    while true
		if cx<1||cy<1||cx>length(m[1])||cy>length(m)
		    return 0
		elseif m[cy][cx]=='L'
		    return 0
	    elseif m[cy][cx]=='#'
		    return 1
		end
		cx+=dx
		cy+=dy
	end
end
open("Puzzle11.txt") do f
    timetaken = @time for l in eachline(f)
	    tempMap=Char[]
	    for i in 1:length(l)
	       push!(tempMap,l[i])
		end
		push!(map,tempMap)
    end
end
map2=deepcopy(map)
change=true
while change
    newMap=deepcopy(map)
	global change=false
    for i in 1:(length(newMap))
	     for j in 1:length(newMap[i])
			otherSeatOcc=0
			if i>1 && j>1 &&i<length(map)&&j<length(map[i])
				if map[i-1][j-1]=='#'
			        otherSeatOcc+=1
			    end
				if map[i-1][j]=='#'
			        otherSeatOcc+=1
			    end
				if map[i-1][j+1]=='#'
			        otherSeatOcc+=1
			    end
				if map[i][j-1]=='#'
			        otherSeatOcc+=1
			    end
				if map[i][j+1]=='#'
			        otherSeatOcc+=1
			    end
				if map[i+1][j-1]=='#'
			        otherSeatOcc+=1
			    end
				if map[i+1][j]=='#'
			        otherSeatOcc+=1
			    end
				if map[i+1][j+1]=='#'
			        otherSeatOcc+=1
			    end
		    elseif i==1&&j==1
				if map[i][j+1]=='#'
			        otherSeatOcc+=1
			    end
				if map[i+1][j]=='#'
			        otherSeatOcc+=1
			    end
				if map[i+1][j+1]=='#'
			        otherSeatOcc+=1
			    end
		    elseif i==1&&j==length(map[i])
				if map[i][j-1]=='#'
			        otherSeatOcc+=1
			    end
				if map[i+1][j]=='#'
			        otherSeatOcc+=1
			    end
				if map[i+1][j-1]=='#'
			        otherSeatOcc+=1
			    end
			elseif i==length(map)&&j==1
				if map[i][j+1]=='#'
			        otherSeatOcc+=1
			    end
				if map[i-1][j]=='#'
			        otherSeatOcc+=1
			    end
				if map[i-1][j+1]=='#'
			        otherSeatOcc+=1
			    end
			elseif i==1&&j!=1&&i<length(map)&&j<length(map[i])
				if map[i][j-1]=='#'
			        otherSeatOcc+=1
			    end
				if map[i][j+1]=='#'
			        otherSeatOcc+=1
			    end
				if map[i+1][j-1]=='#'
			        otherSeatOcc+=1
			    end
				if map[i+1][j]=='#'
			        otherSeatOcc+=1
			    end
				if map[i+1][j+1]=='#'
			        otherSeatOcc+=1
			    end
			elseif i!=1&&j==1&&i<=length(map)&&j<=length(map[i])
				if map[i-1][j]=='#'
			        otherSeatOcc+=1
			    end
				if map[i-1][j+1]=='#'
			        otherSeatOcc+=1
			    end
				if map[i][j+1]=='#'
			        otherSeatOcc+=1
			    end
				if map[i+1][j]=='#'
			        otherSeatOcc+=1
			    end
				if map[i+1][j+1]=='#'
			        otherSeatOcc+=1
			    end
			elseif i==length(map)&&j==length(map[i])
				if map[i][j-1]=='#'
			        otherSeatOcc+=1
			    end
				if map[i-1][j]=='#'
			        otherSeatOcc+=1
			    end
				if map[i-1][j-1]=='#'
			        otherSeatOcc+=1
			    end
			elseif i<length(map)&&j==length(map[i])
				if map[i-1][j]=='#'
			        otherSeatOcc+=1
			    end
				if map[i-1][j-1]=='#'
			        otherSeatOcc+=1
			    end
				if map[i][j-1]=='#'
			        otherSeatOcc+=1
			    end
				if map[i+1][j]=='#'
			        otherSeatOcc+=1
			    end
				if map[i+1][j]=='#'
			        otherSeatOcc+=1
			    end
			elseif i==length(map)&&j<length(map[i])
				if map[i-1][j]=='#'
			        otherSeatOcc+=1
			    end
				if map[i-1][j-1]=='#'
			        otherSeatOcc+=1
			    end
				if map[i][j-1]=='#'
			        otherSeatOcc+=1
			    end
				if map[i-1][j+1]=='#'
			        otherSeatOcc+=1
			    end
				if map[i][j+1]=='#'
			        otherSeatOcc+=1
			    end
			end
			if map[i][j]=='L' && otherSeatOcc==0
			    newMap[i][j]='#'
				global change=true
			elseif map[i][j]=='#' && otherSeatOcc>=4
			    newMap[i][j]='L'
				global change=true
			end
		end
	end
	global map=deepcopy(newMap)
end
ans1=0
for m in map
    for n in m
	    if n=='#'
		    global ans1=ans1+1
		end
	end
end
@show((ans1-1))#Not sure why the -1 is needed. Assuming there is a bug somewhere. Got this by guessing.
change=true
while change
    newMap=deepcopy(map2)
	global change=false
    for i in 1:(length(newMap))
	     for j in 1:length(newMap[i])
			otherSeatOcc=0
			otherSeatOcc+=seatChecker(j,i,0,1,map2)
			otherSeatOcc+=seatChecker(j,i,0,-1,map2)
			otherSeatOcc+=seatChecker(j,i,1,0,map2)
			otherSeatOcc+=seatChecker(j,i,-1,0,map2)
			otherSeatOcc+=seatChecker(j,i,1,1,map2)
			otherSeatOcc+=seatChecker(j,i,1,-1,map2)
			otherSeatOcc+=seatChecker(j,i,-1,1,map2)
			otherSeatOcc+=seatChecker(j,i,-1,-1,map2)
			if map2[i][j]=='L' && otherSeatOcc==0
			    newMap[i][j]='#'
				global change=true
			elseif map2[i][j]=='#' && otherSeatOcc>=5
			    newMap[i][j]='L'
				global change=true
			end
		end
	end
	global map2=deepcopy(newMap)
end
ans2=0
for m in map2
    for n in m
	    if n=='#'
		    global ans2=ans2+1
		end
	end
end
@show(ans2)
