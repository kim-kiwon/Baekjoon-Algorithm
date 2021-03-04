#min heap과 max heap 사용.
#우측힙 모든 원소가 좌측힙 보다 크도록.
#우측=min_heap 좌측=max_heap. heappop을 통해 비교해나가며 규칙유지.
#max_heap 최대값이 중간값이 됨.
import heapq
import sys
n = int(sys.stdin.readline())

left_heap = [] #max heap
right_heap = [] #min heap
for _ in range(n):
    num = int(sys.stdin.readline())
    if len(left_heap) > len(right_heap):
        heapq.heappush(right_heap, num)
    else:
        heapq.heappush(left_heap, -num) #음수를 곱해 max_heap 구현
    if len(left_heap) >= 1 and len(right_heap) >= 1:
        if right_heap[0] < -left_heap[0]:
            r_v = heapq.heappop(right_heap)
            l_v = heapq.heappop(left_heap)
            heapq.heappush(right_heap, -l_v)
            heapq.heappush(left_heap, -r_v)
    print(-left_heap[0])