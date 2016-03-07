import sys
roots = {}
multiplicity = -1 
if len(sys.argv) >= 2:
	args = sys.argv
	key = str(args[1])
	length=len(key)
	keyLets = ''.join(sorted(key))
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

	if key in roots[keyLets]:
		print roots[keyLets], len(roots[keyLets])
	else:
		print "That keyword isn't in our dictionary!"
else: 
	print "ERROR: Please enter a length for the words you seek."