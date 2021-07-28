"""
Created on Wed Jul 28 10:03:48 2021
Python Implementation

NPTEL 
Getting Started with Competitive Programming
Week 1
Mod 1
Reversort
https://www.craft.do/s/AcEMNb4NLdHlQo/b/66FE59A3-D17C-45C9-9C2A-A1C4C76A99E9/Module_1._Reversort

by
https://rajkumargalaxy.github.io/profile

Submission successful at https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d0a5c
"""

# How many cases we expect?
T = int(input())
arrays = []
# read all the input cases and store as list
for c in range(T):
    _ = input()
    arrays.append(list(map(int, input().split())))
    
costs = []
# iterate over all cases
for c in range(T):
    arr = arrays[c]
    # be ready to accumulate the cost
    cost = 0
    # iterate over elements of the array from 0 to N-1
    for i in range(len(arr)-1):
        # find the minimum element in the sub array
        minimum = min(arr[i:])
        # find its index
        pos = arr.index(minimum)
        # reverse the array from i to pos
        arr = arr[:i]+arr[i:pos+1][::-1]+arr[pos+1:]
        cost += pos-i+1
    costs.append(cost)
# output
for c in range(T):
    print(f'Case #{c+1}: {costs[c]}')
    
    
