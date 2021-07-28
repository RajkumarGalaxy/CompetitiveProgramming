T = int(input())
arrays = []
for i in range(T):
    _ = input()
    arrays.append(list(map(int, input().split())))
    
costs = []
for i in range(T):
    arr = arrays[i]
    cost = 0
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
for i in range(T):
    print(f'Case #{i+1}: {costs[i]}')
    
    