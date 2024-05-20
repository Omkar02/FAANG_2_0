"""
* TYPE             : Graph
* ALGORITHM        : Union Find

* TIME-COMPLEXITY  : O(N x M)
* SPACE-COMPLEXITY : O(N x M)



* Example 1:
    Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John",
        "johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
    Output: [
            ["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
            ["Mary","mary@mail.com"],
            ["John","johnnybravo@mail.com"]
            ]
    Explanation:
        The first and second John's are the same person as they have the common email "johnsmith@mail.com".
        The third John and Mary are different people as none of their email addresses are used by other accounts.
        We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
        ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
* Example 2:
    Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co",
        "Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
    Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co",
        "Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
"""


class UnionFind:
    def __init__(self):
        self._relationship = {}

    def union(self, child: int, parent: int) -> None:
        _parent = self.findParent(parent)
        _child = self.findParent(child)
        self._relationship[_child] = _parent

    def findParent(self, child: int) -> int:
        # * IF THERE ARE NO PARENT TO A CHILD
        # * THE CHILD IS THE PARENT
        # * THE IMIDIAGTE NEXT LINE DOES IT .....
        parent = self._relationship.get(child, child)
        if parent != child:
            parent = self.findParent(parent)
            self._relationship[child] = parent
        return parent


def accountsMerge(accounts: list[list[str]]) -> list[list[str]]:
    ownership = {}
    UF = UnionFind()

    # * HERE WE UNPACK THE ACCOUNT'S ARR TO
    #   * _ = FIRST_NAME AND *emails = IS A LIST OF ALL THE MAIL IDS.
    # * THEN TAKIN A SET SO EACH VALUE IS UNIQUE
    for idx, (_, *emails) in enumerate(accounts):
        for email in emails:
            if email in ownership:
                UF.union(ownership[email], idx)
            ownership[email] = idx
    # ! IDX HERE IS NEDED AS THE OWNER NAME CAN BE SIMILAR AS SEEN IN Eg.1
    # ! TO AVOID MERGING OF NON SIMILAR ACCOUNT WE NEED TO HAVE A UNIQUE ID.

    # print(ownership)
    # print(UF._relationship)

    res = {}
    for (email, owner_idx) in ownership.items():
        parent = UF.findParent(owner_idx)
        if parent not in res:
            res[parent] = []
        res[parent].append(email)

    return [[accounts[owner_idx][0], *sorted(emails)] for owner_idx, emails in res.items()]


[print(x) for x in accountsMerge(accounts=[
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]])]

print(accountsMerge(accounts=[["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
                              ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
                              ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
                              ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
                              ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]]))
