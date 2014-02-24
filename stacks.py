#! /usr/bin/python
# stack implementation in python.
# gods i love python!!

class Stack:
  """
  Time Complexity : append and pop both run
  with a O(1) time complexity - meaning this algorithm
  will perform in constant time no matter the item count.
  to reverse the algorithm and use indexing (insert and pop)
  will run O(n) for a stack of size n.
  """
  def __init__(self):
    self.items = []

  def push(self,item):
    # add item to stack - mind LIFO
    self.items.append(item)

  def pop(self):
    # pull first item from stack
    return self.items.pop()

  def peek(self):
    # peek at top of stack but dont remove
    return self.items[len(self.items)-1]

  def isEmpty(self):
    # looks to see if there are any items in stack. boolean.
    return self.items == []

  def size(self):
    # returns the number of items in stack
    return len(self.items)
