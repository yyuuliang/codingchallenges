'''
File: Reverse-a-doubly-linked-list.py
Source: hackerrank
Author: yyuuliang@github
-----
File Created: Thursday, 12th March 2020 4:21:54 pm
Last Modified: Thursday, 12th March 2020 4:21:58 pm
-----
Copyright: MIT
'''


# Reverse a doubly linked list
# https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=linked-lists

# Sample Input
# 4
# 1
# 2
# 3
# 4
# Sample Output
# 4 3 2 1 


#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the reverse function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

# use recursion to solve the problem
class node:
    data=0
    nextnode=None
    prevnode=None
    def __init__(self, dvalue):
        self.data=dvalue
    def printvalue(self):
        print(self.data)

def printlinkedlist(head):
    while head is not None:
        head.printvalue()
        head=head.nextnode


# double linked list
def reversedoublelinkedlist(head):
    if head is None:
        return None
    tmp=reversedoublelinkedlist(head.nextnode)
    if tmp is not None:
        tmp.nextnode=head
        tmp.nextnode.prevnode=tmp
        tmp.nextnode.nextnode=None
        return tmp.nextnode    
    else:
        tmp=head
        tmp.prevnode=None
        tmp.nextnode=None
    return tmp


def reverse(head):
    tail =reversedoublelinkedlist(head)
    # con=None
    while tail.prevnode is not None:
        # con=tail.prevnode
        tail=tail.prevnode
    return tail

n=node(1)
n2=node(2)
n3=node(3)
n4=node(4)
n.nextnode=n2
n2.nextnode=n3
n3.nextnode=n4
n2.prevnode=n
n3.prevnode=n2
n4.prevnode=n3

printlinkedlist(n)
t=reverse(n)
printlinkedlist(t)

# now I want to practice to reverse linkedlist in recursion
# which means dont use prev

