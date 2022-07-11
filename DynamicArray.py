#!/bin/python3

import math
import os
import random
import re
import sys

#
# completed teh dynamic array in pythonn
#things I learnt:
#how to declare an empty 2D array in python without numpy
#
#

def dynamicArray(n, queries):
    # Write your code here
    ans=[]
    arr= [[] for _ in range(n)]
    la = 0
    for i in range(len(queries)):
        
        if(queries[i][0]==1):
            idx = ((queries[i][1]^la)%n)
            arr[idx].append(queries[i][2])
        else:
            idx = ((queries[i][1]^la)%n)
            la=arr[idx][queries[i][2]%len(arr[idx])] 
            ans.append(la)
    return(ans)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
