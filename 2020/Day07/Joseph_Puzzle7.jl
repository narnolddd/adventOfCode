using LightGraphs, SimpleWeightedGraphs
using GraphPlot
function bagCount(edgeList,currentNode,mult)
	bagCounter=0
    for e in edgeList
	    if currentNode==e[1]
		    bagCounter+=(e[3]*mult)+bagCount(edgeList,e[2],mult*e[3])
		end
	end
	return bagCounter
end
bags=[]
edges=[]
open("Puzzle7.txt") do f
    timetaken = @time for l in eachline(f)
		words=split(l," ")
		entry=""
		source=""
		weight=0
		for w in words
		    if w!="bag"&&w!="bags"&&w!="bag."&&w!="bags."&&w!="bag,"&&w!="bags,"&&w!="no"&&w!="other"&&w!="contain"&&isnothing(tryparse(Int32,w))
			    entry=string(entry,w, " ")
			end
			if !isnothing(tryparse(Int64,w))
			   weight=parse(Int64,w)
            end			   
			if w=="bag" ||w=="bags" ||w=="bag." || w=="bags."||w=="bag,"||w=="bags,"
			    if entry!=""
			        push!(bags,strip(entry))
					if source==""
					    source=entry
					else
					    push!(edges,(strip(source),strip(entry),weight))
					end
				end
				entry=""
			end
		end
    end
end
bags=unique(bags)
bagdict=Dict{String,Int}()
for (i,bag) in enumerate(bags)
   push!(bagdict,bag=>i)
end
sources=Int64[]
destinations=Int64[]
weights=Int64[]
for e in edges
    push!(sources,bagdict[e[1]])
	push!(destinations,bagdict[e[2]])
	push!(weights,e[3])
end
DAG = SimpleWeightedDiGraph(sources,destinations,weights)
ans1=0
for b in bags
    if b!="shiny gold"&&has_path(DAG,bagdict[b],bagdict["shiny gold"])
	   global ans1= ans1 +1
	end
end
@show(ans1)
ans2=bagCount(edges,"shiny gold",1)
@show(ans2)
