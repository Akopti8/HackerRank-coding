#!/bin/python3

import math
import os
import random
import re
import sys
import bisect
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player,ranlen, playlen):
    # Write your code here
    #below we project a new array
    #we first fo the set operation to remove any duplicates 
    #list operation projects into rank
    #finally we sort it 
    rank = sorted(list(set(ranked)))
    out=[]
    ranlen= len(rank)
    #I have noticed that during bisection, is the value at the returned index is equal then the level is: ranlen-temp otherwise we add 1 to ranlen becuse it wouldn't duplicate level 
    for i in range(playlen):
        temp = bisect.bisect_left(rank,player[i])
        if(temp == ranlen):
            out.append(int(1))
        elif(rank[temp]==player[i]):
            out.append(((ranlen)-temp))
        elif(rank[temp]!=player[i]):
            out.append(((ranlen+1)-temp))
    #level array creator 
    return(out)       
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player,ranked_count,player_count)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
