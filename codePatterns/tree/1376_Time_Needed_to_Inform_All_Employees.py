"""
* Example 1:
    Input: n = 1, headID = 0, manager = [-1], informTime = [0]
    Output: 0
    Explanation: The head of the company is the only employee in the company.
* Example 2:
    Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
    Output: 1
    Explanation: The head of the company with id = 2 is the direct manager of all the employees in the company and needs 1 minute to inform them all.
        The tree structure of the employees in the company is shown.
"""


# ! NOTE THIS IS MORE LIKE A GRAPH PROBLEM
# ! BUT USES A BFS TO CALCULATE

def numOfMinutes(n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
    emp_manager_map = {}
    for emp_id in range(n):
        _manager = manager[emp_id]
        if _manager not in emp_manager_map:
            emp_manager_map[_manager] = []
        emp_manager_map[_manager].append(emp_id)

    # print(emp_manager_map)

    q = [(-1, 0)]  # (head_of_company, time_raken)
    max_time = 0
    while q:
        cur_head, cur_time = q.pop(0)
        max_time = max(max_time, cur_time)
        if cur_head in emp_manager_map:
            for sub_worker in emp_manager_map[cur_head]:
                # * ADDING THE CUR_TIME AND SUB_WORKER TIME
                q.append([sub_worker, cur_time + informTime[sub_worker]])
    return max_time


print(numOfMinutes(n=1,
                   headID=0,
                   manager=[-1],
                   informTime=[0]))
print('-' * 50)
print(numOfMinutes(n=6,
                   headID=2,
                   manager=[2, 2, -1, 2, 2, 2],
                   informTime=[0, 0, 1, 0, 0, 0]))
