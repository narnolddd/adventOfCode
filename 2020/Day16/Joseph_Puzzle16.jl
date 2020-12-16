ranges=[]
yourTicket=[]
otherTickets=[]
inputCounter=0
open("Puzzle16.txt") do f
    timetaken = @time for l in eachline(f)
	     if l ==""
		    @show("Skipping Empty line")
		 elseif l=="your ticket:"
		    global inputCounter=inputCounter+1
		 elseif l=="nearby tickets:"
		    global inputCounter=inputCounter+1
	     elseif inputCounter==0
		     sp=split(l,":")[2]
			 sp=split(sp," or ")
			 for s in sp
			     ra=split(s,"-")
				 for r in ra
			         push!(ranges,parse(Int,r))
				 end
		     end
		 elseif inputCounter==1
		    sp=split(l,",")
		    for s in sp
			     push!(yourTicket,parse(Int,s))
		    end
		 elseif inputCounter==2
		    sp=split(l,",")
			ticket=[]
		    for s in sp
			     push!(ticket,parse(Int,s))
		    end 
			push!(otherTickets,ticket)
         end				 
    end
end
validTickets=[]
ans1=0
for ticket in otherTickets
    validTicket=true
	for t in ticket
	    valid=false
	    for i in 1:2:length(ranges)
		    if t>=ranges[i]&&t<=ranges[i+1]
			    valid=true
			end
		end
		if valid==false
		    validTicket=false
		    global ans1= ans1+t
		end
	end
	if validTicket
	    push!(validTickets,ticket)
	end
end
@show(ans1)
for i in 1:20
    possibilities=[true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true]
    for v in validTickets
	    test=v[i]
		for j in 1:4:length(ranges)
		    if ((test>=ranges[j]&&test<=ranges[j+1])||(test>=ranges[j+2]&&test<=ranges[j+3]))==false
			    possibilities[floor(Int,j/4)+1]=false
			end
		end
	end
	@show(i)
	@show(possibilities)
end
ans2=yourTicket[1]*yourTicket[2]*yourTicket[4]*yourTicket[8]*yourTicket[9]*yourTicket[15]#Figured this out from the print above
@show(ans2)
