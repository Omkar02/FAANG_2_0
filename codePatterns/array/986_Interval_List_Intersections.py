"""
* Example 1:
    Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
    Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
* Example 2:
    Input: firstList = [[1,3],[5,9]], secondList = []
    Output: []
"""


def intervalIntersection(firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
    first_idx = second_idx = 0
    first_len, second_len = len(firstList), len(secondList)

    intersections = []

    while first_idx < first_len and second_idx < second_len:
        """
        * Explanaition
            ?firstList =  [ [0, 2], [5, 10], [13, 23], [24, 25] ]
            ?secondList = [ [1, 5], [8, 12], [15, 24], [25, 26] ]
        * Ouput
            ?[ [1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25] ]
                * For [1, 2] = [ high(firstList[i][0], secondList[j][0]) , low(firstList[i][1], secondList[j][1]
        """

        start = max(firstList[first_idx][0], secondList[second_idx][0])
        end = min(firstList[first_idx][1], secondList[second_idx][1])

        if start <= end:
            # * The equal is for to take care [5, 5] condition..
            intersections.append([start, end])

        if firstList[first_idx][1] < secondList[second_idx][1]:
            first_idx += 1
        else:
            second_idx += 1
    print(intersections)
    return intersections


assert intervalIntersection(
    firstList=[[0, 2], [5, 10], [13, 23], [24, 25]],
    secondList=[[1, 5], [8, 12], [15, 24], [25, 26]]) == [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]

assert intervalIntersection(firstList=[[1, 3], [5, 9]], secondList=[]) == []
