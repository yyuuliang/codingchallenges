'''
File: Fraudulent-Activity-Notifications.py
Source: hackerrank
Author: yyuuliang@github
-----
File Created: Friday, 6th March 2020 11:55:35 am
Last Modified: Friday, 6th March 2020 11:56:04 am
-----
Copyright: MIT
'''

#
# Fraudulent Activity Notifications
# https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
#
#
##

# counting sort

# mp is the position we want to find in the array
# here it is the middle one or each of the middle two
def findmedian(ca,mp):
    cp = mp+1
    median=0
    for i in range(len(ca)):
        if ca[i]>0:
            cp-=ca[i]
        if cp<=0:
            median=i
            break
    return median

def findmm(ca,d):
    m=0
    if d%2 ==1:
        m=findmedian(ca,int(d/2))
    else:
        m1=findmedian(ca,d/2)
        m2=findmedian(ca,d/2-1)
        m=(m1+m2)/2
    return m
 
def activityNotifications(expenditure, d):
    # generate the first count array
    ca =[0]*(max(expenditure)+1)
    for n in expenditure[0:d]:
        ca[n]+=1
    # find median from the counting array
    m=findmm(ca,d)
    # compare with next
    idx = d
    p=0
    idx_pop=0
    if expenditure[idx]>=m*2:
        p+=1
    # then we start the rolling
    for n in expenditure[d:]:
        # print(ca)
        # pop  the front item
        ca[expenditure[idx_pop]]-=1
        idx_pop+=1
        # add the idx one
        ca[n]+=1
        # compute the median of the new ca
        m=findmm(ca,d)
        # compare with next
        idx+=1
        if idx < len(expenditure) and expenditure[idx]>=m*2:
            p+=1
    return p

a=[2, 3, 4, 2, 3, 6, 8, 4, 5] 
d=5
print(a)
p=activityNotifications(a,d)
print(p)