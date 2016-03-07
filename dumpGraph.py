import sys
import json
roots = {}
counter = 0
with open('../lenSortedEngWords.txt') as inputfile:
	for line in inputfile:
		word = line[:-1]
		if len(word)>counter:
			print word, counter
			counter +=1
		s = ''.join(sorted(word))
		if s in roots.keys():
			roots[s].append(word)
		else:
			roots[s] = [word]
with open('anagraphDict.json', 'w') as f:
	f.write(json.dumps(roots))
f.close()
print "done"
