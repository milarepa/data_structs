#!/usr/bin/python3
"""
Search a sorted list
"""
import math as m

# Binary Search

def binary_search(item,l):

  mid = m.floor(len(l) / 2)

  if item == l[mid]:
    return True
  else:
    left, right = l[:mid], l[mid:]

  if item < mid:
    return binary_search(item,left)
  else:
    return binary_search(item,right)


if __name__ == '__main__':
  item = 5
  l = [x for x in range(1,20)]

  print(binary_search(item,l))
