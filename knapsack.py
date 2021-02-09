# 반복문
def knapsack1(capacity, n, size, value):
    array = [[0 for _ in range(capacity + 2)] for _ in range(n + 2)]
    for i in range(1, n + 1):
        for s in range(1, capacity + 1):
            if size[i-1] > s: # 물건의 부피가 s보다 크면
                array[i][s] = array[i-1][s]
            else: # 물건의 부피가 s보다 작거나 크면
                array[i][s] = max(value[i-1] + array[i-1][s-size[i-1]], array[i-1][s])
    return array[n][capacity]

# 재귀
def knapsack2(capacity, n, size, value):
    if capacity == 0 or n == 0:
        return 0
    if size[n-1] > capacity:
        return knapsack2(capacity, n - 1)
    else:
        return max(value[n-1] + knapsack2(capacity-size[n-1], n-1), knapsack2(capacity, n-1))

"""
size = [9, 3, 4, 7, 8]
value = [13, 4, 5, 10, 11]
print(knapsack1(10, 5)) # 14
"""
