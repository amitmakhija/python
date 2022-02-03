'''
There are N (N > 0) beggars sitting in a row outside a temple. Each beggar initially has an empty pot. 
When the devotees come to the temple, they donate some amount of coins to these beggars. 
Each devotee gives a fixed amount of coin(according to his faith and ability) to some K beggars sitting next to each other.

Given the amount donated by each devotee to the beggars ranging from i to j index, where 1 <= i <= j <= N, 
find out the final amount of money in each beggar's pot at the end of the day, provided they don't fill their pots by any other means.
'''


N = 5 # No. of beggars
D = [[1, 2, 10], [2, 3, 20], [2, 5, 25]] # Donations by devotees

import numpy as np

#create array of amount held by beggars initially

#beg = np.zeros(N)
beg = np.full(shape=N,fill_value=0,dtype=np.int)

#Convert the list of Donations to array
D = np.array(D)

for i in range(len(D)):
    beg[range(D[i,0]-1,D[i,1])] = beg[range(D[i,0]-1,D[i,1])] + D[i,2]
    
print(beg)