'''
File: Common-Child.py
Source: hackerrank
Author: yyuuliang@github
-----
File Created: Monday, 9th March 2020 8:14:40 pm
Last Modified: Monday, 9th March 2020 8:14:49 pm
-----
Copyright: MIT
'''


# Complete the commonChild function below.
# https://en.wikipedia.org/wiki/Longest_common_subsequence_problem

# Sample Input

# HARRY
# SALLY
# Sample Output

#  2

# regular running time, this will pass all tests in PYPY3
def commonChild(s1, s2):
    m=len(s1)+1
    n=len(s2)+1
    # this is wrong
    # r=[[0]*m]*n
    r=[0]*m
    start =1
    m_end=m
    n_end=n
    for i in range(m):
        r[i]=[0]*n
    # trim the start position
    trim = 0
    while start<m-2 and start<n-2 and s1[start-1]==s2[start-1]:
        start+=1
        trim+=1
    while start<m_end and start<n_end and s1[m_end-2]==s2[n_end-2]:
        m_end-=1
        n_end-=1
        trim+=1
    for i in range(start,m_end):
        for j in range(start,n_end):
            if s1[i-1]==s2[j-1]:
                r[i][j]=r[i-1][j-1]+1
            else:
                r[i][j]=max(r[i-1][j],r[i][j-1])
    return r[m_end-1][n_end-1]+trim
    
# optimized running time

s1='WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS'
s2='FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC'

s1='abcd'
s2='abdc'

result = commonChild(s1, s2)
print(result)
result = commonChild(s2, s1)
print(result)