'''
File: Count-Triplets.py
Source: hackerrank
Author: yyuuliang@github
-----
File Created: Wednesday, 11th March 2020 12:12:19 pm
Last Modified: Wednesday, 11th March 2020 12:12:33 pm
-----
Copyright: MIT
'''


# Complete the countTriplets function below.
# https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps


import math
from collections import defaultdict

def countTriplets(arr,r):
    # we wanna find ABC,B=A*2, C=B*2
    # this is the expecting-B dict
    expecting2=defaultdict(int)
    # this is the expecting-C dict
    expecting3=defaultdict(int)
    counter=0
    for n in arr:
        # if n is C, we can get the actual pair number
        counter+=expecting3[n]
        # if n is B, we update the expecting-C dict, the number means how many pairs of AB are ready, if we have a C, they can compose the ABC pair immedinately. 
        expecting3[n*r]+=expecting2[n]
        # if n ic A, we update the expecing-B dict, the number means how many A are ready, if we have a B, they can compose the AB pair immedinately.
        expecting2[n*r]+=1
        print(n)
        print(expecting2)
        print(expecting3)
        print(counter)

    return counter

def countTriplets2(arr, r):

    # put list into dict
    # arr.sort()
    # d={}
    p={}
    for i in range(len(arr)):
        n=arr[i]
        if n in p:
            # d[n]+=1
            p[n].append(i)
        else:
            # d[n]=1
            p[n]=[i]
    # print(d)
    # print(p)
    counter=0
    ma =max(p)
    if r==1:
        for n in p:
            f=math.factorial
            l = len(p[n])
            if l>3:
                counter+= int(f(l)/(f(l-3)*f(3)))
    else:
        for n in p:
            if n<=ma:
                if n*r in p and n*r*r in p:
                    # counter+=d[n]*d[n*r]*d[n*r*r]
                    a1=p[n]
                    for p1 in a1:
                        m2=0
                        a2=p[n*r]
                        for p2 in a2:
                            m3=0
                            if p2>p1:
                                m2+=1
                                a3=p[n*r*r]
                                for p3 in a3:
                                    if p3>p2:
                                        m3+=1
                        counter+=m2*m3

                    
    return counter


    return count
s='1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1'
ss=s.split(' ')
arr=[]
for c in ss:
    arr.append(int(c))
arr=[2,1, 2, 1, 2, 4,8]
r=2
ans = countTriplets(arr, r)
print(ans)