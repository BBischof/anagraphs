# Anagraph

Trying to visualize the graph of all words with edges given by "are anagrams of one another". 

## Subsets

I am considering changing the graph to also have nodes if one word is a subset of another word. It might be amusing to look at this way, and slightly more interesting. 

## How it was created

Read through the list of words, sorted the word, looked if the sorted version of the word was in my hash, if so, I added it to the list stored in that value of the hash. 

### Arguments

The script is called `makeAnagraph.py`.

The first argument is the integer length of the words you're interested in.

The second argument(optional), is the number of anagrams you're looking for. If not included, the script returns all of the words in the largest set of anagrams.

If you want to look at the graph in a bigger way, first run `dumpGraph.py` (or look at the one I already dumped into anagraphDict.json). Then your `makeAnagraph.py` can load this large JSON automatically, and create a full graph. This `secret` function can be found by eschewing both parameters whne you call it.

#### E.g.

Input:
```
> python makeAnagraph.py 10
```

Output:
```
['underserve', 'underverse', 'undeserver', 'unreserved', 'unreversed']
```

whereas 

Input:
```
> python makeAnagraph.py 10 4
```

Output:
```
['aeromantic', 'cameration', 'maceration', 'racemation']
['alpestrine', 'episternal', 'interlapse', 'presential']
['creational', 'crotalinae', 'laceration', 'reactional']
['arctoidean', 'carotidean', 'cordaitean', 'dinocerata']
```

### Data

Here is a simple histogram of the maximum multiplicity of anagrams of length `n` in my corpus. 

```
2 	== 2
3 	===== 5
4 	======== 8
5 	========== 10
6 	========= 9
7 	======= 7
8 	======= 7
9 	===== 5
10	===== 5
11	===== 5
12	=== 3
13	=== 3
14	== 2
15	==== 4
16	== 2
17	== 2
18	== 2
19	== 2
20	== 2
21	== 2
22	== 2
```

### Lonely words

We can use the original to find lonely words, which are simply words that don't have any anagrams. 

```
> python makeAnagraph.py 10 1
```
which outputs a lot. In fact, it outputs `28742` words. It'd be amusing to look at the ratio of words in my corpus to lonely words. 

Here is a table of the data:

| Length 	| Lonelys 	| Total 	| Ratio        	|
|--------	|---------	|-------	|--------------	|
| 2      	| 59      	| 139   	| 0.4244604317 	|
| 3      	| 489     	| 1294  	| 0.3778979907 	|
| 4      	| 2204    	| 4994  	| 0.4413295955 	|
| 5      	| 5475    	| 9972  	| 0.5490373045 	|
| 6      	| 11216   	| 17462 	| 0.6423090139 	|
| 7      	| 17954   	| 23713 	| 0.7571374352 	|
| 8      	| 25021   	| 29842 	| 0.8384491656 	|
| 9      	| 28734   	| 32286 	| 0.8899832745 	|
| 10     	| 28742   	| 30824 	| 0.9324552297 	|
| 11     	| 24909   	| 25963 	| 0.9594037669 	|
| 12     	| 19889   	| 20447 	| 0.972709933  	|
| 13     	| 14673   	| 14923 	| 0.9832473363 	|
| 14     	| 9621    	| 9761  	| 0.9856572073 	|
| 15     	| 5832    	| 5922  	| 0.9848024316 	|
| 16     	| 3307    	| 3377  	| 0.9792715428 	|
| 17     	| 1769    	| 1813  	| 0.9757308329 	|
| 18     	| 822     	| 842   	| 0.9762470309 	|
| 19     	| 414     	| 428   	| 0.9672897196 	|
| 20     	| 192     	| 198   	| 0.9696969697 	|
| 21     	| 74      	| 82    	| 0.9024390244 	|
| 22     	| 37      	| 41    	| 0.9024390244 	|
| 23     	| 17      	| 17    	| 1            	|
| 24     	| 5       	| 5     	| 1            	|

And here is a histograms of those percentages:

```
2 =============== 42 %
3 ========== 37 %
4 ================= 44 %
5 =========================== 54 %
6 ===================================== 64 %
7 ================================================ 75 %
8 ======================================================== 83 %
9 ============================================================= 88 %
10 ================================================================== 93 %
11 ==================================================================== 95 %
12 ====================================================================== 97 %
13 ======================================================================= 98 %
14 ======================================================================= 98 %
15 ======================================================================= 98 %
16 ====================================================================== 97 %
17 ====================================================================== 97 %
18 ====================================================================== 97 %
19 ===================================================================== 96 %
20 ===================================================================== 96 %
21 =============================================================== 90 %
22 =============================================================== 90 %
23 ========================================================================= 100 %
24 ========================================================================= 100 %
```

#### Making less lonely words

I wanted to let words have more friends, so I looked at the graph of words where two words are `friends` iff they're anagrams of one another or one of the two words is an anagram of the set of letters with one removed. This is similar to the word ladder puzzle, but where order doesn't matter. 

I was happy to see that it reduces the overall number of `less lonely` words significantly from those that are just `lonely`. 


| Length 	| Lonelys 	| Total 	| Ratio        	|
|--------	|---------	|-------	|--------------	|
| 2  | 1    | 139   | 0.007194244604 |
| 3  | 78   | 1294  | 0.06027820711  |
| 4  | 353  | 4994  | 0.07068482179  |
| 5  | 1127 | 9972  | 0.113016446    |
| 6  | 2755 | 17462 | 0.1577711602   |
| 7  | 4803 | 23713 | 0.202547126    |
| 8  | 6943 | 29842 | 0.232658669    |
| 9  | 7742 | 32286 | 0.2397943381   |
| 10 | 6879 | 30824 | 0.2231702569   |
| 11 | 5146 | 25963 | 0.1982051381   |
| 12 | 3214 | 20447 | 0.1571868734   |
| 13 | 1801 | 14923 | 0.1206861891   |
| 14 | 808  | 9761  | 0.08277840385  |
| 15 | 336  | 5922  | 0.05673758865  |
| 16 | 156  | 3377  | 0.0461948475   |
| 17 | 75   | 1813  | 0.04136789851  |
| 18 | 30   | 842   | 0.03562945368  |
| 19 | 16   | 428   | 0.03738317757  |
| 20 | 8    | 198   | 0.0404040404   |
| 21 | 6    | 82    | 0.07317073171  |
| 22 | 3    | 41    | 0.07317073171  |
| 23 | 0    | 17    | 0              |
| 24 | 0    | 5     | 0              |


Here is a histogram of these percentages(to overall words):

```
2	= 0 %
3	====== 6 %
4	======= 7 %
5	=========== 11 %
6	=============== 15 %
7	==================== 20 %
8	======================= 23 %
9	======================= 23 %
10	====================== 22 %
11	=================== 19 %
12	=============== 15 %
13	============ 12 %
14	======== 8 %
15	===== 5 %
16	==== 4 %
17	==== 4 %
18	=== 3 %
19	=== 3 %
20	==== 4 %
21	======= 7 %
22	======= 7 %
23	= 0 %
24	= 0 %
```

## Anagrams of a particular word

I added the script `keyWordAnagram.py` which takes one argument, a word, and finds the list of its anagrams.

### E.g.

```
> python keyWordAnagrams.py reliant
```
```
['entrail', 'latiner', 'latrine', 'ratline', 'reliant', 'retinal', 'trenail'] 7
```
```
> python keyWordAnagrams.py anagram
```
```
['anagram'] 1

```
```
> python keyWordAnagrams.py anagrams
```
```
['anagrams'] 1

```
```
> python keyWordAnagrams.py anagraph
```
```
['anagraph'] 1
```
A little dissapointing that these are all so lonely.
