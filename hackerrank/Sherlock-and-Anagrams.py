'''
File: Sherlock-and-Anagrams.py
Source: hackerrank
Author: yyuuliang@github
-----
File Created: Tuesday, 10th March 2020 9:07:09 pm
Last Modified: Tuesday, 10th March 2020 9:07:20 pm
-----
Copyright: MIT
'''

# Sherlock and Anagrams
# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps


def sherlockAndAnagrams(s):
    alld={}
    for i in range(len(s)):
        n=s[i]
        # print(n)

        if n in alld:
            alld[n]+=1
        else:
            alld[n]=1
        for j in range(i+1,len(s)):
            n+=s[j]
            # print(n)
            # this is to build a new string with sorted order chars
            nl=list(n)
            nl.sort()
            nn=''
            for x in nl: 
                nn+= x  
            if nn in alld:
                alld[nn]+=1
            else:
                alld[nn]=1
    cc=0
    for k in alld:
        kk=alld[k]
        cc+=kk*(kk-1)/2
    # print(alld)
    return cc


s='cdcd'
result = sherlockAndAnagrams(s)
print(result)