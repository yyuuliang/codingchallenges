'''
File: Special-String-Again.py
Source: hackerrank
Author: yyuuliang@github
-----
File Created: Saturday, 7th March 2020 6:42:26 pm
Last Modified: Saturday, 7th March 2020 6:42:34 pm
-----
Copyright: MIT
'''


#
# string
# https://www.hackerrank.com/challenges/special-palindrome-again/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
#

# Sample Input 0

# 5
# asasd
# Sample Output 0

# 7 

# con number sum
def conp(n):
    return int(n*(n+1)/2)

# Complete the substrCount function below.
def substrCount(n, s):
    # print(n,s)
    cpl=1
    suma=0
    ls=len(s)
    for i in range(ls):
        if i+1<ls and s[i]==s[i+1]:
            cpl+=1
        else:
            # contiuous stop
            suma+=conp(cpl)
            for j in range(cpl):
                if i+j+2<ls and s[i-j]==s[i+j+2]:
                    suma+=1
                else:
                    break
            cpl=1

    return suma



n=7
s='aabaa'
result = substrCount(n, s)
print(result)
