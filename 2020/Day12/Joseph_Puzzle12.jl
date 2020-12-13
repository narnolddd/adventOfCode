dir=String[]
x=0
y=0
angle=0
open("Puzzle12.txt") do f
    timetaken = @time for l in eachline(f)
	     push!(dir,l)
    end
end
for i in 1:(length(dir))
    if dir[i][1]=='F'
	    global x=x+(parse(Int,dir[i][2:length(dir[i])])*cos(deg2rad(angle)))
		global y=y+(parse(Int,dir[i][2:length(dir[i])])*sin(deg2rad(angle)))
	elseif dir[i][1]=='L'
	    global angle=angle+parse(Int,dir[i][2:length(dir[i])])
    elseif dir[i][1]=='R'		
	    global angle=angle-parse(Int,dir[i][2:length(dir[i])])
	elseif dir[i][1]=='N'
	    global y=y+parse(Int,dir[i][2:length(dir[i])])
	elseif dir[i][1]=='S'
	    global y=y-parse(Int,dir[i][2:length(dir[i])])
	elseif dir[i][1]=='E'
	    global x=x+parse(Int,dir[i][2:length(dir[i])])
	elseif dir[i][1]=='W'
	    global x=x-parse(Int,dir[i][2:length(dir[i])])
	end
end
ans1=abs(x)+abs(y)	
@show(ans1)
x=0
y=0
wx=10
wy=1
for i in 1:(length(dir))
    if dir[i][1]=='F'
	    global x=x+(parse(Int,dir[i][2:length(dir[i])])*wx)
		global y=y+(parse(Int,dir[i][2:length(dir[i])])*wy)
	elseif dir[i][1]=='L'
	    tAng=parse(Int,dir[i][2:length(dir[i])])
		tx=wx
		ty=wy
		global wx=tx*cos(deg2rad(tAng))-ty*sin(deg2rad(tAng))
		global wy=tx*sin(deg2rad(tAng))+ty*cos(deg2rad(tAng))
    elseif dir[i][1]=='R'		
	    tAng= parse(Int,dir[i][2:length(dir[i])])*-1
		tx=wx
		ty=wy
		global wx=tx*cos(deg2rad(tAng))-ty*sin(deg2rad(tAng))
		global wy=tx*sin(deg2rad(tAng))+ty*cos(deg2rad(tAng))
	elseif dir[i][1]=='N'
	    global wy=wy+parse(Int,dir[i][2:length(dir[i])])
	elseif dir[i][1]=='S'
	    global wy=wy-parse(Int,dir[i][2:length(dir[i])])
	elseif dir[i][1]=='E'
	    global wx=wx+parse(Int,dir[i][2:length(dir[i])])
	elseif dir[i][1]=='W'
	    global wx=wx-parse(Int,dir[i][2:length(dir[i])])
	end
end
ans2=abs(x)+abs(y)
@show(ans2)	
