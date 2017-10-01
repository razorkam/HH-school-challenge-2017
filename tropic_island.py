import heapq
from collections import deque


class Heap:  # std heapq wrapper (min-heap)
    def __init__(self):
        self._data = []

    def push(self, r, c, value):
        heapq.heappush(self._data, (value, r, c))

    def pop(self):
        return heapq.heappop(self._data)[1:3]

    def not_empty(self):
        return bool(self._data)


# island is a list of lists
#  island = [
#      [2, 2, 2],
#      [2, 1, 2],
#      [2, 1, 2],
#      [2, 1, 2]
#  ]

def get_water_volume(island):
    m = len(island)
    n = len(island[0])
    hp = Heap()
    # visited = [[False] * n] * m
    visited = [[False] * n for _ in range(m)]
    for row, sublist in enumerate(island):  # push outer boundary to the heap
        hp.push(row, 0, sublist[0])
        visited[row][0] = True
        hp.push(row, n - 1, sublist[-1])
        visited[row][n-1] = True
        if row in {0, m - 1}:
            for col, val in enumerate(sublist[1:-1]):
                hp.push(row, col+1, val)
                visited[row][col+1] = True

    volume = 0
    while hp.not_empty():
        cur = hp.pop()
        volume += bfs(island, visited, cur, hp)

    return volume


def bfs(island, visited, start_xy, heap):
    m = len(island)
    n = len(island[0])
    q = deque([start_xy])  # xy is a tuple (x,y)
    start_value = island[start_xy[0]][start_xy[1]]
    volume = 0
    while q:
        vertex = q.popleft()
        x = vertex[0]
        y = vertex[1]
        neighbours = [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]
        for nei in neighbours:
            if m - 1 > nei[0] > 0 and n - 1 > nei[1] > 0 and \
                    not visited[nei[0]][nei[1]]:
                value = island[nei[0]][nei[1]]
                if value <= start_value:
                    volume += start_value - value
                    q.append((nei[0], nei[1]))
                else:
                    heap.push(nei[0], nei[1], value)

                visited[nei[0]][nei[1]] = True

    return volume


if __name__ == '__main__':
    # isl = [
    #      [5,3,4,5],
    #      [6,2,1,4],
    #      [3,1,1,4],
    #      [8,5,4,3]
    #         ]
    isl = [[1,600,3],
           [600,5,600],
           [7,800,9]]
    print(get_water_volume(isl))


# def spoj():
#     try:
#         tests = input()
#         for i in range(int(tests)):
#             l = []
#             size = input().split(' ')
#             for j in range(int(size[0])):
#                 row = list(map(int, input().split(' ')))
#                 l.append(row)
#             print(get_water_volume(l))
#             input()
#     except EOFError:
#         return 0
#
# spoj()