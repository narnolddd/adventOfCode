pas=String[]
lEdge=Int32[]
uEdge=Int32[]
tChar=Char[]
open("Puzzle2.txt") do f
    timetaken = @time for l in eachline(f)
        sl=split(l," ")
	    push!(lEdge,parse(Int32,split(sl[1],"-")[1]))
	    push!(uEdge,parse(Int32,split(sl[1],"-")[2]))
	    push!(tChar,sl[2][1])
           push!(pas,sl[3])
    end
end
@show(lEdge)
@show(uEdge)
@show(tChar)
@show(pas)
ans1=0
for i in 1:length(lEdge)
    occCount=count(a->(a==tChar[i]),pas[i])
    if occCount>=lEdge[i] && occCount<=uEdge[i]
        global ans1= ans1+1
    end
end
@show(ans1)

ans2=0
for i in 1:length(lEdge)
    count=0
    if pas[i][lEdge[i]]==tChar[i]
        count+=1
    end
	if pas[i][uEdge[i]]==tChar[i]
        count+=1
    end
	if count==1
	    global ans2 = ans2+1
    end
end
@show(ans2)
