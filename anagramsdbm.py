import anydbm,pickle
from itertools import permutations
def anaenc(x):
	db=anydbm.open('anagrams','c')
	for y in x:
		db[y]=pickle.dumps([''.join(p) for p in permutations(y)])
	return db
p=anaenc(['abhilash','qweer'])
print pickle.loads(p['abhilash'])
