'''
File: Frequency-Queries.py
Source: hackerrank
Author: yyuuliang@github
-----
File Created: Wednesday, 11th March 2020 8:14:11 pm
Last Modified: Wednesday, 11th March 2020 8:14:21 pm
-----
Copyright: MIT
'''


#
# Complete the countTriplets function below.    
# https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
#


# Sample Input 1

# 4
# 3 4
# 2 1003
# 1 16
# 3 1
# Sample Output 1

# 0
# 1

import math
from collections import defaultdict


# Complete the freqQuery function below.
# use two dictionary to save time
def freqQuery(queries):
    # print(queries)
    ret=[]
    d=defaultdict(int)
    df=defaultdict(int)
    for a in queries:
        if a[0]==1:
            df[d[a[1]]]-=1
            d[a[1]]+=1
            df[d[a[1]]]+=1
        if a[0]==2:
            if d[a[1]]>0:
                df[d[a[1]]]-=1
                d[a[1]]-=1
                df[d[a[1]]]+=1
        if a[0]==3:
            if df[a[1]]>0:
                ret.append(1)
            else:
                ret.append(0)

    return ret

# Complete the freqQuery function below.
# this will be time out on test 11
def freqQuery2(queries):
    # print(queries)
    ret=[]
    d=defaultdict(int)
    for a in queries:
        if a[0]==1:
            d[a[1]]+=1
        if a[0]==2:
            if d[a[1]]>0: 
                d[a[1]]-=1
            if d[a[1]]==0:
                d.pop(a[1])
        if a[0]==3:
            vs=set(list(d.values()))
            if a[1] in vs:
                ret.append(1)
            else:
                ret.append(0)
    return ret



q=[[1, 5], [1, 6], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5], [3, 2]]
ret=freqQuery(q)
print(ret)

