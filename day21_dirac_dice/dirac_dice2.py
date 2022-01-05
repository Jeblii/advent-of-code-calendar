#!/usr/bin/python3
import sys
import heapq
import itertools
import re
import ast
from collections import defaultdict, Counter, deque

# p1 = 7-1
# p2 = 2-1
p1 = 4-1
p2 = 8-1
die = 0

def roll():
  global die
  die += 1
  return die

s1 = 0
s2 = 0
while True:
  print(s1, s2)
  m1 = roll() + roll() + roll()
  p1 = (p1 + m1) % 10
  s1 += p1+1
  if s1 >= 1000:
    print(s2*die)
    break

  m2 = roll() + roll() + roll()
  p2 = (p2+m2)%10
  s2 += p2+1
  if s2 >= 1000:
    print(s1*die)
    break

