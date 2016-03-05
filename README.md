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
2 =============== 42
3 ========== 37
4 ================= 44
5 =========================== 54
6 ===================================== 64
7 ================================================ 75
8 ======================================================== 83
9 ============================================================= 88
10 ================================================================== 93
11 ==================================================================== 95
12 ====================================================================== 97
13 ======================================================================= 98
14 ======================================================================= 98
15 ======================================================================= 98
16 ====================================================================== 97
17 ====================================================================== 97
18 ====================================================================== 97
19 ===================================================================== 96
20 ===================================================================== 96
21 =============================================================== 90
22 =============================================================== 90
23 ========================================================================= 100
24 ========================================================================= 100
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
