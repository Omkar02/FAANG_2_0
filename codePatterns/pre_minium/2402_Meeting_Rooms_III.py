"""
    * Time Complexity   : O(NLogN)
    * Space Complexity  : O(N)
    * Date              : 2, June 2024
"""

"""
* Example 1:

    Input: n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
    Output: 0
    Explanation:
        - At time 0, both rooms are not being used. The first meeting starts in room 0.
        - At time 1, only room 1 is not being used. The second meeting starts in room 1.
        - At time 2, both rooms are being used. The third meeting is delayed.
        - At time 3, both rooms are being used. The fourth meeting is delayed.
        - At time 5, the meeting in room 1 finishes. The third meeting starts in room 1 for the time period [5,10).
        - At time 10, the meetings in both rooms finish. The fourth meeting starts in room 0 for the time period [10,11).
        Both rooms 0 and 1 held 2 meetings, so we return 0. 
* Example 2:
    Input: n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
    Output: 1
    Explanation:
        - At time 1, all three rooms are not being used. The first meeting starts in room 0.
        - At time 2, rooms 1 and 2 are not being used. The second meeting starts in room 1.
        - At time 3, only room 2 is not being used. The third meeting starts in room 2.
        - At time 4, all three rooms are being used. The fourth meeting is delayed.
        - At time 5, the meeting in room 2 finishes. The fourth meeting starts in room 2 for the time period [5,10).
        - At time 6, all three rooms are being used. The fifth meeting is delayed.
        - At time 10, the meetings in rooms 1 and 2 finish. The fifth meeting starts in room 1 for the time period [10,12).
        Room 0 held 1 meeting while rooms 1 and 2 each held 2 meetings, so we return 1. 
"""




import heapq
def mostBooked(n: int, meetings: list[list[int]]) -> int:
    meetings.sort()  # Sort the meetings on the start_time

    # Maintain a state using min_heap
    available = [i for i in range(n)]
    used_room = []  # (end_time, room_id)
    # -------------------------------

    count = [0] * n  # used room count
    for start, end in meetings:
        # * Step 3: If meeting is overed
        while used_room and used_room[0][0] <= start:
            # if pre_end_time is less than eq to cur_start_time
            _, room = heapq.heappop(used_room)
            heapq.heappush(available, room)

        # * Step 2: If no room is available to accomadete the meet
        # *         This will cause a delay
        if not available:
            end_time, room_id = heapq.heappop(used_room)
            # make the room available
            heapq.heappush(available, room_id)
            # schedule the next meet with delay from ended meet
            end = end_time + (end - start)

        # * Step 1: Assigning lowest no availabel room
        room = heapq.heappop(available)
        heapq.heappush(used_room, (end, room))

        count[room] += 1
    # print(count)
    return count.index(max(count))


print(mostBooked(n=2, meetings=[[0, 10], [1, 5], [2, 7], [3, 4]]))
print(mostBooked(n=3, meetings=[[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]))
