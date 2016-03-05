import sys
roots = {}
multiplicity = -1 
if len(sys.argv) >= 2:
	args = sys.argv
	length = int(args[1])
	if len(sys.argv) >=3:
		multiplicity = int(args[2])
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
			print roots[b]
else: 
	print "ERROR: Please enter a length for the words you seek."