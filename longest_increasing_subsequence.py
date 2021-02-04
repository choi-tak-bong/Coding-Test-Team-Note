from typing import List

def longest_increasing_subsequence(n: int, array: List[int]):
    dp = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if array[j] < array[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)
