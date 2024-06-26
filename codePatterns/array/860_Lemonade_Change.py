"""
* Example 1:
    Input: bills = [5,5,5,10,20]
    Output: true
    Explanation: 
        From the first 3 customers, we collect three $5 bills in order.
        From the fourth customer, we collect a $10 bill and give back a $5.
        From the fifth customer, we give a $10 bill and a $5 bill.
        Since all customers got correct change, we output true.
* Example 2:
    Input: bills = [5,5,10,10,20]
    Output: false
    Explanation: 
        From the first two customers in order, we collect two $5 bills.
        For the next two customers in order, we collect a $10 bill and give back a $5 bill.
        For the last customer, we can not give the change of $15 back because we only have two $10 bills.
        Since not every customer received the correct change, the answer is false.

"""


def lemonadeChange(bills: list[int]) -> bool:
    five = ten = 0
    for b in bills:
        if b == 5:
            five += 1
        elif b == 10:
            if not five:
                return False
            ten += 1
            five -= 1
        else:
            # for 20
            if ten and five:
                five -= 1
                ten -= 1

            elif five >= 3:
                five -= 3
            else:
                return False
    return True


print(lemonadeChange(bills=[5, 5, 5, 10, 20]))
print(lemonadeChange(bills=[5, 5, 10, 10, 20]))


# class Solution:
#     def lemonadeChange(self, bills: List[int]) -> bool:
#         five = ten = 0
#         for bill in bills:
#             if bill == 5: five += 1
#             elif bill == 10:
#                 if not five: return False
#                 five, ten = five - 1, ten + 1
#             else:
#                 if ten and five:
#                     five, ten = five - 1, ten - 1
#                 elif five >= 3: five -= 3
#                 else: return False
#         return True
