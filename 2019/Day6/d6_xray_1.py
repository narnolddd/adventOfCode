#!python

from pprint import pprint

#处理输入，分割
def GetData(name = "input.txt"):
	data = []
	with open(name,'r') as fin:
		for line in fin:
			data.append((line.rstrip()).split(")"))

	return data

#构造树形结构
def GetOrbitTree(data):
	treemap = {}

	for item in data:
		if treemap.get(item[0]) == None:
			treemap[item[0]] = {'father':' ', 'child':[item[1]]}
		else:
			treemap[item[0]]['child'].append(item[1])

		if treemap.get(item[1]) == None:
			treemap[item[1]] = {'father':item[0], 'child':[]}
		else:
			treemap[item[1]]['father'] =item[0]  #认为只有一个唯一father

	return treemap

#确定父节点位置
def GetRootNode(tree):
	roots = []
	for key in tree:
		if tree[key]['father'] == ' ':
			roots.append(key)

	return roots

#---------------------------------------------------------#
#遍历
def DFS_Count(father, level,  tree):
	size = len(tree[father]['child'])
	count = 0
	if size !=0:
		count += len(tree[father]['child'])*level
		for item in tree[father]['child']:
			count += DFS_Count(item, level+1,  tree)

	return count

#Part1 求轨道数量
def CountOribits(tree):
	roots = GetRootNode(tree)

	count = 0
	for root in roots:
		count += DFS_Count(root, 1,  tree)

	return count


#----------------------------------------------------------#
def FindRootToYOUPath(tree, root, endyou, youpath):
	youpath.append(root)
	if endyou in tree[root]['child']:
		return 1

	if tree[root]['child'] == []:
		youpath.pop()
		return 0

	for key in tree[root]['child']:
		if FindRootToYOUPath(tree, key, endyou, youpath):
			return 1

	youpath.remove(root)

# part2 求最短路
def GetMiniPathNumber(path1, path2):
	for i in range(0, min(len(path1), len(path2))):
		if path1[i] != path2[i]:
			return len(path1)+len(path2) - i*2

	
#--------------------------------------------------------#
'''
def RUNPARTONE(name = 'input.txt'):
	re = GetData(name)
	tree = GetOrbitTree(re)
	print(CountOribits(tree))
'''
def RUNPARTTWO(name , stname, endname):
	re = GetData(name)
	tree = GetOrbitTree(re)
	roots = GetRootNode(tree)

	YOU = []
	SAN = []
	FindRootToYOUPath(tree, roots[0], stname, YOU)
	FindRootToYOUPath(tree, roots[0], endname, SAN)

	print(GetMiniPathNumber(YOU, SAN))


RUNPARTTWO('input.txt' , 'YOU', 'SAN')
