from collections import defaultdict
from itertools import permutations
#from time import time
import timeit

def sortword(word):
	return ''.join(sorted(list(word.lower())))

def permword(word):
	return set([''.join(p) for p in permutations(word)])

anagram = defaultdict(list)
words = open('linuxwords.txt').read().split()
for w in words: anagram[sortword(w)].append(w)

while True:
	try:
		w = input('\nEnter anagram: ')
	except:

		break
	if not w: break

	start_time = timeit.default_timer()
	answer = anagram[sortword(w)]
	end_time = timeit.default_timer()
	elapsed_time = end_time - start_time

	print ('Anagram Lookup: {:0.4f}ms "{}" --> {}'.format(elapsed_time * 1000, w, anagram[sortword(w)]))

	answer = []
	count = 0
	start_time = timeit.default_timer()
	for p in permword(w):
		count += 1
		if p in words:
			answer += [w]
	end_time = timeit.default_timer()
	elapsed_time = end_time - start_time

	print ('Dictionary Lookup of {} permutations: {:0.4f}s "{}" --> {}'.format(count, elapsed_time, w, anagram[sortword(w)]))

print ('\nExiting.')