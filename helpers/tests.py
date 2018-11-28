import to_game
print("""""")
x = [0,0,0,1,1,2,2]
print (to_game.majority(x) == 2)

x = [0,0,0,1,1,1,2]
print (to_game.majority(x) == 1)

x = [0,0,0,1,2,2,2]
print (to_game.majority(x) == 2)

# x = [0,0,0]
# print (to_game.majority(x) == 2)

import helper
from collections import Counter

A = helper.load_pickle('A_org.pickle') #as is
b = helper.load_pickle('b_org.pickle')
occrs = Counter(b).most_common
print(occrs)

A = helper.load_pickle('A_nod.pickle') #remove dup
b1 = helper.load_pickle('b_nod.pickle')
occrs = Counter(b1).most_common
print(occrs)

A = helper.load_pickle('A_avg.pickle') #remove dup and calc avg
b2 = helper.load_pickle('b_avg.pickle')
occrs = Counter(b2).most_common
print(occrs)
print(b1==b2)
