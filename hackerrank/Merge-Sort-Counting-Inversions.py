'''
File: Merge-Sort-Counting-Inversions.py
Source: hackerrank
Author: yyuuliang@github
-----
File Created: Friday, 6th March 2020 11:57:20 am
Last Modified: Friday, 6th March 2020 11:57:22 am
-----
Copyright: MIT 
'''

#
# Merge Sort: Counting Inversions
# https://www.hackerrank.com/challenges/ctci-merge-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
#

# merge sort

# Sample Input

# 2  
# 5  
# 1 1 1 2 2  
# 5  
# 2 1 3 1 2
# Sample Output

# 0  
# 4   

def countInversions(a):
    if len(a)>1:
        m=int(len(a)/2)
        la=a[0:m]
        ra=a[m:]
        s1=countInversions(la)
        s2=countInversions(ra)
        # now merge left and right together
        ll=len(la)
        lr=len(ra)
        li, ri,mi =0,0,0
        swap=0
        # swap happens here
        if s1 is not None:
            swap +=s1
        if s2 is not None:
            swap +=s2
        while True:
            if la[li]>ra[ri]:
                # to move from right to the most-front left, we have to cross (ll-li) numbers
                # whcih means (ll-li) swaps
                swap+=(ll-li)
                a[mi]=ra[ri]
                ri+=1
            else:
                a[mi]=la[li]
                li+=1
            mi+=1
            if li==ll:
                # put the rest of R
                for n in ra[ri:]:
                    a[mi]=n
                    mi+=1
                break
            if ri==lr:
                # put the rest of L
                for n in la[li:]:
                    a[mi]=n
                    mi+=1
                break
        return swap
        
a=[12, 11, 13, 5, 6, 7]
# a=[2 ,1, 3, 1, 2]
sw=countInversions(a)
print(a,sw)