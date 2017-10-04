import heapq
from collections import deque


class Heap:  # std heapq wrapper (min-heap)
    def __init__(self):
        self._data = []

    def push(self, r, c, value):
        heapq.heappush(self._data, (value, r, c))  # heap stores value(key) + row and column indices

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
    visited = [[False] * n for _ in range(m)]

    # push island outer boundary to the heap and mark it as visited [no need to run bfs from]
    for row in {0, m - 1}:
        for col, val in enumerate(island[row]):
            hp.push(row, col, val)
            visited[row][col] = True

    for row, sublist in enumerate(island[1:-1]):
        for col in {0, n - 1}:
            hp.push(row + 1, col, sublist[col])
            visited[row + 1][col] = True

    volume = 0
    while hp.not_empty():
        cur = hp.pop()
        volume += bfs(island, m, n, visited, cur, hp)

    return volume


def bfs(island, m, n, visited, start_xy, heap):  # run breadth first search from cell and found cells to be flooded
    q = deque([start_xy])  # xy is a tuple (x,y)
    start_value = island[start_xy[0]][start_xy[1]]
    volume = 0
    while q:
        vertex = q.popleft()
        x = vertex[0]
        y = vertex[1]
        adjacent = ((x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1))
        for a in adjacent:
            row = a[0]
            col = a[1]
            if not (m > row > 0 and n > col > 0):
                continue

            if not visited[row][col]:
                value = island[row][col]
                if value <= start_value:
                    volume += start_value - value
                    q.append((row, col))
                else:
                    heap.push(row, col, value)

                visited[row][col] = True

    return volume


if __name__ == '__main__':

    isl = [               # simple test
        [5, 3, 4, 5],
        [6, 2, 1, 4],
        [3, 1, 1, 4],
        [8, 5, 4, 3]
    ]

    print(get_water_volume(isl))
