import heapq


def solution(scoville, K):
    if scoville[0] == 0:
        return -1
    num = 0
    heapq.heapify(scoville)
    while scoville[0] < K:

        least_spicy = heapq.heappop(scoville)
        s_least_spicy = heapq.heappop(scoville)
        new = least_spicy + 2 * s_least_spicy
        heapq.heappush(scoville, new)
        num += 1
        if len(scoville) == 1 and scoville[0] < K:
            return -1

    return num