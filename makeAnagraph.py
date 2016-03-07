import sys
import json
import networkx as nx 
roots = {}
multiplicity = -1 
length = -1
start = ''.join(sorted("life"))
end = ''.join(sorted("death"))

def makeGraph():
	with open('anagraphDict.json') as data_file:    
		data = json.load(data_file)
	g = nx.Graph()
	gdict = {}
	for word in data.keys():
			if len(word)==1:
				gdict[word]=[]
			else:
				gdict[word]=[]
				for i in range(len(word)):
					sub = word[:i] + "" + word[i+1:]
					if sub in gdict:
						#gdict[sub].append(word)
						g.add_edge(sub, word)
					else:
						g.add_node
	return g, data

if len(sys.argv) >= 2:
	args = sys.argv
	length = int(args[1])
	if len(sys.argv) >=3:
		multiplicity = int(args[2])
	if length != -1:
		with open('../lenSortedEngWords.txt') as inputfile:
			for line in inputfile:
				word = line[:-1]
				if len(word) == length:
					s = ''.join(sorted(word))
					# print s
					if s in roots.keys():
						roots[s].append(word)
					else:
						roots[s] = [word] 

		if multiplicity != -1:
			for k in roots.keys():
				if len(roots[k]) == multiplicity:
					print roots[k]
		else:
			max = 1
			best = []
			for k in roots.keys():
				if len(roots[k]) > max:
					max = len(roots[k])
					best = [k]
				elif len(roots[k]) == max:
					best.append(k)
			for b in best:
				print roots[b], len(roots[b])
else:
	g, roots = makeGraph()
	# for p in nx.all_shortest_paths(g, start, end):
	# 	print p, len(p)
	# for node in min(nx.connected_components(g), key=len):
	# 	#print roots[str(node)]
	# 	print roots[str(node)]

	# littles = [c for c in sorted(nx.connected_components(g), key=len, reverse=False) if len(c)<3]
	# for x in littles:
	# 	for i in [a for a in x if len(roots[a])==1]:
	# 		print len(x), str(i), [str(s) for s in roots[i]]


## maybe here I could look at what words are a concatenations of 
## two large(relative) words, so they're essentially just portmanteus

	degs = g.degree()
	lonelies = [n for n in degs if degs[n]==1]
	out = []
	for l in lonelies:
		if len(roots[l]) == 1:
			# print l, str(roots[l][0])
			out.append(str(roots[l][0]))
	print len(sorted(out, key=len, reverse=False))
# else: 
# 	print "ERROR: Please enter a length for the words you seek."
