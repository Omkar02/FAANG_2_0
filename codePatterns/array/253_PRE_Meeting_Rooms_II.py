"""
*_Example 1:
    Input: [[0, 30],[5, 10],[15, 20]]
    Output: 2
* Example 2:
    Input: [[7,10],[2,4]]
    Output: 1
"""
import heapq


def meetingRoomTwo(timings: list[list[int, int]]):
    # this is a stack based approach
    occupied_rooms = []
    # sort timings based on starting time..
    timings.sort(key=lambda x: x[0])

    for new_meet in timings:
        if occupied_rooms and new_meet[0] > occupied_rooms[0]:
            heapq.heappop(occupied_rooms)
            heapq.heappush(occupied_rooms, new_meet[-1])
        else:
            heapq.heappush(occupied_rooms, new_meet[-1])

    return len(occupied_rooms)


print(meetingRoomTwo(timings=[[0, 30], [5, 10], [15, 20]]))
print(meetingRoomTwo(timings=[[7, 10], [2, 4]]))



