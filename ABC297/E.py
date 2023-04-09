N, K = map(int, input().split())
A = list(map(int, input().split()))



def bit_subset_sum(arr):
    new_array = []
    n = len(arr)
    ans = float('inf')  
    
    for i in range(1, 2**n):
        subset = []
        for j in range(n):
          if (i >> j) & 1:
            subset.append(arr[j]) 
        subset_sum = sum(subset) 
        new_array.append(subset_sum) 

    return new_array


result = bit_subset_sum(A)
result.sort()
print(len(result)) 


# 溶けてない