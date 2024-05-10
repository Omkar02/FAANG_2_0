"""
? Pattern: Minimum (Maximum) Path to Reach a Target
? Approach: Priority Queue

* Example 1:
    Input: target = 1, startFuel = 1, stations = []
    Output: 0
    Explanation: We can reach the target without refueling.
* Example 2:
    Input: target = 100, startFuel = 1, stations = [[10,100]]
    Output: -1
    Explanation: We can not reach the target (or even the first gas station).
* Example 3:
    Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
    Output: 2
    Explanation: We start with 10 liters of fuel.
        We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
        Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
        and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
        We made 2 refueling stops along the way, so we return 2.
"""
import heapq


def minRefuelStops(target, startFuel, stations):
    # Convert stations into a max heap for efficient retrieval of the largest element
    pq = []

    # Initialize variables: stops as 0 and current fuel as startFuel
    stops, curr_fuel = 0, startFuel

    # Iterate through each station while there are still stations and current fuel is less than target
    i = 0
    while curr_fuel < target:
        # Check if we can reach this station with our current fuel
        while i < len(stations) and curr_fuel >= stations[i][0]:
            # If yes, add its fuel to max heap (as negative value for max heap) and remove it from stations list
            heapq.heappush(pq, -stations[i][1])
            i += 1

        # If we can't reach the next station but have some fuel in max heap,
        # refuel using the station with maximum available fuel
        if not pq:
            return -1
        curr_fuel += -heapq.heappop(pq)
        stops += 1

    return stops


print(minRefuelStops(target=1, startFuel=1, stations=[]))
print(minRefuelStops(target=100, startFuel=1, stations=[[10, 100]]))
print(minRefuelStops(target=100, startFuel=10,
      stations=[[10, 60], [20, 30], [30, 30], [60, 40]]))
