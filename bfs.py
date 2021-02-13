"""
출처 : 이것이 코딩 테스트다 with 파이썬 (나동빈 지음, 한빛미디어 출판)
너비 우선 탐색. 가까운 노드부터 탐색하는 방식. 선입선출 방식의 큐를 이용.
"""

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

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

bfs(graph, 1, visited)
"""
