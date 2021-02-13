"""
출처: 이것이 코딩 테스트다 with 파이썬 (나동빈 지음, 한빛미디어 출판)
깊이 우선 탐색. 최대한 멀리 있는 노드를 우선으로 탐색하는 방식. 스택 자료구조 이용.
"""

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

"""
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited)
"""
