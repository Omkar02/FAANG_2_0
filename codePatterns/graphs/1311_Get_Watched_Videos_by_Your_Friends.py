"""
* TYPE             : Graph
* ALGORITHM        : BFS 

* TIME-COMPLEXITY  :
* SPACE-COMPLEXITY :

* Example 1:
    Input: watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 1
    Output: ["B","C"] 
    Explanation: 
        You have id = 0 (green color in the figure) and your friends are (yellow color in the figure):
        Person with id = 1 -> watchedVideos = ["C"] 
        Person with id = 2 -> watchedVideos = ["B","C"] 
        The frequencies of watchedVideos by your friends are: 
        B -> 1 
        C -> 2
* Example 2:
    Input: watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 2
    Output: ["D"]
    Explanation: You have id = 0 (green color in the figure) and the only friend of your friends 
        is the person with id = 3 (yellow color in the figure).
"""
from collections import Counter


def watchedVideosByFriends(watchedVideos, friends, id, level):
    """
    * Using BFS to find all friends at the given level

    INTTUINO HERE THIS IS AN SIMPLE BFS SOLUTION WHERE IN THE ASK OF THE QUESTION 
    IS NOTHING BUT ON LEVEL RETURN THE ALL THE MOVIES SORTED BY FREQ COUNT.
    """
    q = [(id, 0)]
    vistited = set([id])
    videos = []
    while q:
        # * CUR_FRIEND HERE IS AN IDX
        cur_friend, cur_level = q.pop(0)

        if cur_level == level:
            # * ADDING ALL VIDEOS FOR THAT FRIEND AT THE REQ LEVEL
            # ! NO NEED TO GO FURTHERE FOR THE RESPECTIVE FRD. THAT'S WHY IF & ELSE
            videos.extend(watchedVideos[cur_friend])

        else:
            for next_friend in friends[cur_friend]:
                if next_friend not in vistited:
                    vistited.add(next_friend)
                    q.append((next_friend, cur_level + 1))

    # * COUNT THE FREQ OF EACH MOVIES
    video_count = Counter(videos)

    # * SORTING VIDEOS BY FREQ AND THEN ALPHA.
    return sorted(video_count.keys(), key=lambda x: (video_count[x], x))


print(watchedVideosByFriends(watchedVideos=[["A", "B"], ["C"], ["B", "C"], ["D"]],
                             friends=[[1, 2], [0, 3], [0, 3], [1, 2]],
                             id=0,
                             level=1))

print(watchedVideosByFriends(watchedVideos=[["A", "B"], ["C"], ["B", "C"], ["D"]],
                             friends=[[1, 2], [0, 3], [0, 3], [1, 2]],
                             id=0,
                             level=2))
