# Anagraph

Trying to visualize the graph of all words with edges given by "are anagrams of one another". 

## Subsets

I am considering changing the graph to also have nodes if one word is a subset of another word. It might be amusing to look at this way, and slightly more interesting. 

## How it was created

Read through the list of words, sorted the word, looked if the sorted version of the word was in my hash, if so, I added it to the list stored in that value of the hash. 

### Arguments

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