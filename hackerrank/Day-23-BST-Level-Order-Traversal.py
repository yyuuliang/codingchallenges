'''
File: Day-23-BST-Level-Order-Traversal.py
Source: hackerrank
Author: yyuuliang@github
-----
File Created: Friday, 6th March 2020 11:00:23 pm
Last Modified: Friday, 6th March 2020 11:01:04 pm
-----
Copyright: MIT
'''

# binary search tree
# Day 23: BST Level-Order Traversal
# https://www.hackerrank.com/challenges/30-binary-trees/problem

import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        # use a queue to store each level
        q=[]
        a=[]
        q.append(root)
        while len(q)>0:
            croot=q.pop(0)
            a.append(croot.data)
            # print(croot.data)
            if croot.left is not None:
                q.append(croot.left)
            if croot.right is not None:
                q.append(croot.right)
        for n in a:
            print(n, end =" ")

T=6
myTree=Solution()
a=[3,5,4,7,2,1]
root=None
for i in range(T):
    data=a[i]
    root=myTree.insert(root,data)
myTree.levelOrder(root)