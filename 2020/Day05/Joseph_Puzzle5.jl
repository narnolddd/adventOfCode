seats=[]
open("Puzzle5.txt") do f
    entry=""
    timetaken = @time for l in eachline(f)
		push!(seats,l)
    end
end
ans1=0
filledSeats=[]
for s in seats
    uRB=127
	lRB=0
	uSB=7
	lSB=0
	rowID=0
	seatID=0
    for i in 1:length(s)
	    if s[i]=='F'
		    if i!=7
		        uRB=uRB-(128/2^i)
		    else
			    rowID=lRB
		    end
	    elseif s[i]=='B'
		    if i!=7
		        lRB=lRB+(128/2^i)
			else
			    rowID=uRB
		    end
		elseif s[i]=='R'
		    if i!=10
			    lSB=lSB+(8/2^(i-7))
			else
			    seatID=uSB
		    end
		elseif s[i]=='L'
		    if i!=10
			    uSB=uSB-(8/2^(i-7))
			else
			    seatID=lSB
			end
		end
	end
	push!(filledSeats,(floor(rowID*8+seatID)))
	if rowID*8+seatID>ans1
		    global ans1=rowID*8+seatID
	end
end
@show(ans1)
ans2=0
for i in 1:length(filledSeats)
    if !(i in filledSeats)
		global ans2=i#This works for my solution but may not work for others
    end
end
@show(ans2)
