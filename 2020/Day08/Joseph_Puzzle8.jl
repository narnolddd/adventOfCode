instructions=String[]
edges=[]
open("Puzzle8.txt") do f
    timetaken = @time for l in eachline(f)
	     push!(instructions,l)
    end
end
instructionsUtilized=[]
acc=0
pc=1
while !(pc in instructionsUtilized)
    push!(instructionsUtilized,pc)
    s=split(instructions[pc],' ')
	operand=parse(Int32,s[2])
	if s[1]=="nop"
	    global pc = pc +1
	elseif s[1]=="acc"
	    global acc = acc +operand
		global pc =pc +1
	elseif s[1] == "jmp"
	    global pc=pc+operand
	end
end
@show(acc)
pt=false
lc=1
while !pt
    global acc=0
	global pc=1
	global instructionsUtilized=[]
	newInstructions=copy(instructions)
	if occursin("nop",newInstructions[lc])
	    newInstructions[lc]=replace(newInstructions[lc],"nop"=>"jmp")
	elseif occursin("jmp",newInstructions[lc])
	    newInstructions[lc]=replace(newInstructions[lc],"jmp"=>"nop")
	end
	while !(pc in instructionsUtilized)&!pt
	    if pc ==length(instructions)
		    global pt =true
		end
        push!(instructionsUtilized,pc)
        s=split(newInstructions[pc],' ')
	    operand=parse(Int32,s[2])
	    if s[1]=="nop"
	         global pc = pc +1
	    elseif s[1]=="acc"
	         global acc = acc +operand
		     global pc =pc +1
	    elseif s[1] == "jmp"
	        global pc=pc+operand
	    end
    end
	global lc=lc+1
end
@show(acc)

