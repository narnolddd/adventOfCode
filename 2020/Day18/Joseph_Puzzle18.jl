exp=[]
open("Puzzle18.txt") do f
    timetaken = @time for l in eachline(f)
	    push!(exp,l)		
    end	
end
ans1=0
for e in exp
    val=Int128[0,0,0]
	previousOperator=[0,0,0]
	depth=1
	for c in e
	    if c=='*'
		    previousOperator[depth]=2
        elseif c=='+'
     	    previousOperator[depth]=1
		elseif c=='('
		    depth=depth+1
		elseif c==')'
		    if previousOperator[depth-1]==1
			   val[depth-1]=val[depth-1]+val[depth]
			elseif previousOperator[depth-1]==2
			   val[depth-1]=val[depth-1]*val[depth]
			elseif previousOperator[depth-1]==0
			   val[depth-1]=val[depth]
			end
			val[depth]=0
			previousOperator[depth]=0
			depth=depth-1
		elseif c==' '
		    
		else
		    if previousOperator[depth]==1
			   val[depth]=val[depth]+parse(Int128,c)
			elseif previousOperator[depth]==2
			   val[depth]=val[depth]*parse(Int128,c)
			elseif previousOperator[depth]==0
			   val[depth]=parse(Int128,c)
			end
		end
	end
	global ans1+=val[1]
end
println(ans1)
ans2=0
for e in exp
	depth=1
    operands=[]
	operators=[]
	for c in e
	    if c=='*'
		    push!(operators,depth*2)
        elseif c=='+'
     	    push!(operators,depth*2-1)
		elseif c=='('
		    depth=depth+1
		elseif c==')'

			depth=depth-1
		elseif c==' '
		    
		else
            push!(operands,parse(Int,c))
		end
	end
	o=1
	len=length(operators)
	while o<=len
	    if operators[o]==5
		    operands[o]=operands[o]+operands[o+1]
			deleteat!(operands,o+1)
			deleteat!(operators,o)
			len=length(operators)
			o=1
		else
		   o+=1
		end
	end
	len=length(operators)
	o=1
	while o<=len
	    if operators[o]==6
		    operands[o]=operands[o]*operands[o+1]
			deleteat!(operands,o+1)
			deleteat!(operators,o)
			len=length(operators)
			o=1
		else
		    o+=1
		end
	end
	len=length(operators)
	o=1
	while o<=len
	    if operators[o]==3
		    operands[o]=operands[o]+operands[o+1]
			deleteat!(operands,o+1)
			deleteat!(operators,o)
			len=length(operators)
			o=1
		else
		    o+=1
		end
	end
	len=length(operators)
	o=1
	while o<=len
	    if operators[o]==4
		    operands[o]=operands[o]*operands[o+1]
			deleteat!(operands,o+1)
			deleteat!(operators,o)
			len=length(operators)
			o=1
		else
		   o+=1
		end
	end
	len=length(operators)
	o=1
	while o<=len
	    if operators[o]==1
		    operands[o]=operands[o]+operands[o+1]
			deleteat!(operands,o+1)
			deleteat!(operators,o)
			len=length(operators)
			o=1
		else
		    o+=1
		end
	end
	val=operands[1]
	for o in 2:length(operands)
	    val*=operands[o]
	end	
    global ans2=ans2+val	
end
println(ans2)
