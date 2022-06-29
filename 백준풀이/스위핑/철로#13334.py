import sys
import heapq as h
input = sys.stdin.readline
N = int(input())
ele = [sorted(list(map(int, input().split())), reverse=True) for _ in range(N)]
D = int(input())
ele.sort()

crt_dist = 0
crt_node = [0, D + 1]
heap = []
heap_in = []
answer = 0
for i in ele:
    h.heappush(heap, i)

while heap:
    crt_node = h.heappop(heap)
    if abs(crt_node[0] - crt_node[1]) > D:
        continue
    crt_dist = crt_node[0]
    if crt_dist - D <= crt_node[1]:
        h.heappush(heap_in, (crt_node[1], crt_node[0]))
        if crt_dist - D > heap_in[0][0]:
            while heap_in and heap_in[0][0] < crt_dist - D:
                h.heappop(heap_in)
        if answer < len(heap_in):
            answer = len(heap_in)

print(answer)