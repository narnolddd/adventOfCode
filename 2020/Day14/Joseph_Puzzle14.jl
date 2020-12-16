inst=[]
function possibleAddress(add,allAdd)
    xDet=false
	var3=""
	var4=""
    for j in 1:length(add)
	    if add[j]=='X'&&xDet==false
		    var3=var3*'0'
			var4=var4*'1'
			xDet=true
		else
		    var3=var3*add[j]
			var4=var4*add[j]
		end
	end
	if xDet
	    possibleAddress(var3,allAdd)
		possibleAddress(var4,allAdd)
	else
	    push!(allAdd,var3)
	end
end
open("Puzzle14.txt") do f
    timetaken = @time for l in eachline(f)
		push!(inst,l)
    end
end
mask=""
mem=Dict()
for i in inst
    com=split(i," = ")[1]
	vari=split(i," = ")[2]
	if com=="mask"
	    global mask = vari
	else
	    var2=bitstring(parse(UInt64,vari))
		var2=var2[29:length(var2)]
		var3=""
		for j in 1:length(var2)
		    if mask[j]!='X'
			    var3=var3*mask[j]
			else
			    var3=var3*var2[j]
			end
		end
		push!(mem,com=>var3)
	end
end
ans1=0
for (key,value) in mem
    global ans1=ans1+parse(Int,value,base=2)
end
@show(ans1)
mask2=""
mem2=Dict()
for i in inst
    allAddresses=[]
    com=split(i," = ")[1]
	vari=split(i," = ")[2]
	if com=="mask"
	    global mask2 = vari
	else
	    com2=replace(com,"mem["=>"")
		com2=replace(com2,"]"=>"")
	    var2=bitstring(parse(UInt64,com2))
		var2=var2[29:length(var2)]
		var3=""
		for j in 1:length(var2)
		    if mask2[j]=='X'||mask2[j]=='1'
			    var3=var3*mask2[j]
			else
			    var3=var3*var2[j]
			end
		end
		possibleAddress(var3,allAddresses)
		for a in allAddresses
		    push!(mem2,a=>vari)
		end
	end
end
ans2=0
for (key,value) in mem2
    global ans2=ans2+parse(Int,value)
end
@show(ans2)
