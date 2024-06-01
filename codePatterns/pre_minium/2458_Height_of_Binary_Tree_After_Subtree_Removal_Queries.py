"""
    * Time Complexity   : O(NlogN)
    * Space Complexity  : O(N)
    * Date              : 1, June 2024
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeQueries(self, root: TreeNode, queries: list[int]) -> list[int]:
        """
        Intution is to have a map created level, height and cousines where in the cousine
        at same level are sorted base on height

        so if the max node is getting deleted get the hight of next highest and + it with level
        so we get new_max_height

        else the max_height remains the same.
        """

        # * STEP 1: GET LEVEL/DEPTH & HEIGHT FOR EACH NODE
        # *         DEPTH/LEVEL IS DISTANCE FROM ROOT TILL THE RESPECTIVE NODE
        # *         HEIGHT IS DISTANCE FROM RESPICTIVE NODE TILL THE LEAF OF TREE

        level_mapping = {}
        height_mapping = {}

        def compute(node, level):
            if not node:
                return 0

            level_mapping[node.val] = level

            left = compute(node.left, level + 1)
            right = compute(node.right, level + 1)

            height = max(left, right)
            height_mapping[node.val] = height

            # * RETURN HEIGHT + 1 AS WE ARE CALCUTING THE DEPTH
            # * AND HEIGHT IN SAME FUNC.
            # * FOR ROOT THE HEIGHT IS 0 THUS STORING IT AND THEN
            # * UPDATING THE VAL AND RETURNING.
            return 1 + height

        max_height = compute(root, 0) - 1
        print('Level Map = ', level_mapping)
        print('Height Map = ', height_mapping)

        # * STEP 2: GETTING THE COUSINE IN THE SAME LEVEL
        # *         MAKE SURE THESE COUSINE ARE SORTED BASED ON HEIGHT DECS

        cousine = {}
        for node_val, level in level_mapping.items():
            if level not in cousine:
                cousine[level] = []
            cousine[level].append((height_mapping[node_val], node_val))

        for level in cousine:
            cousine[level].sort(reverse=True)

        print('Cousine = ', cousine)

        # * STEP 3: FINAL STEP IF PERFORMING THE QURIES.
        res = []
        for delete_node in queries:
            cur_level_of_delete_node = level_mapping[delete_node]
            cousine_of_delete_delete_node = cousine.get(
                cur_level_of_delete_node)

            if cousine_of_delete_delete_node[0][1] != delete_node:
                # * IT'S NOT THE MAX THAT'S GETTING DELETED SO MAX_HEIGHT STAYS SAME
                res.append(max_height)
            else:
                # * CHECK IF THERE'S A NEXT GREATEST COUSINE NODE BESIDE THE MAX_PATH_NODE_GETTING DELETED.
                if len(cousine_of_delete_delete_node) > 1:
                    height_from_replacement_node = cousine_of_delete_delete_node[1][0]
                else:
                    # * IF NOT RETURN -1
                    height_from_replacement_node = -1

                new_max_height = height_from_replacement_node + cur_level_of_delete_node
                res.append(new_max_height)
        return res
