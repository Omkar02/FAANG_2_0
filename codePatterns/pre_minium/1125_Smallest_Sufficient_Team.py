"""
    * Time Complexity   : O(V+E)
    * Space Complexity  : O(V)
    * Date              : 8, June 2024
"""

"""
* Example 1:
    Input: req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
    Output: [0,2]
* Example 2:
    Input: req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
    Output: [1,2]
"""


def smallestSufficientTeam(self, req_skills: list[str], people: list[list[str]]) -> list[int]:
    len_people = len(people)

    def backtrack(idx: int):
        if idx > len_people:
            return []

        team_skills = []
        for ind_skills in people[idx]:
            if ind_skills in req_skills:
                team_skills.append(ind_skills)
        if team_skills:
            return team_skills

        for jdx in range(idx + 1, len_people):
            pre_skills = backtrack(jdx)


print(smallestSufficientTeam(req_skills=["java", "nodejs", "reactjs"],
                             people=[["java"], ["nodejs"], ["nodejs", "reactjs"]]))

print(smallestSufficientTeam(req_skills=["algorithms", "math", "java", "reactjs", "csharp", "aws"],
                             people=[
                                 ["algorithms", "math", "java"],
                                 ["algorithms", "math", "reactjs"],
                                 ["java", "csharp", "aws"],
                                 ["reactjs", "csharp"],
                                 ["csharp", "math"],
                                 ["aws", "java"]]
                             ))
