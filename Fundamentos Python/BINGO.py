import random

B=list(range(1,16))
I=list(range(16,31))
N=list(range(31,46))
G=list(range(46,61))
O=list(range(61,76))

BINGO=[]

for i in range(15):
    BINGO.append('B'+str(B[i]))
    BINGO.append('I'+str(I[i]))
    BINGO.append('N'+str(N[i]))
    BINGO.append('G'+str(G[i]))
    BINGO.append('O'+str(O[i]))
    
random.shuffle(BINGO)
print(BINGO)
