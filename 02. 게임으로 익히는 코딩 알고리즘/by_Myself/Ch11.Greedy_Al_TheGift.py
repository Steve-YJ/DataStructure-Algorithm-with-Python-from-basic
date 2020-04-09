## Codingame 'The Gift'
## Rules
'''
The Doctor has in hand the list of maximum budgets for each Ood.
The Doctor's aim is to share the cost very precisely. 
To respect the Oods democratic values and to select the best solution.
the Doctor decides that:

* No Ood can be more than his maximum budget
* the optimal solution is the one for which the highest contribution
  is minimal
* If there are several optimal solutions, then the best solution is the one
  for which the highest second contribution is minimal, and so on and so forth...

Moreover, to facilitate the calculations, the Doctor wants each financial
participation to be an integer of the local currency(nobody should give any cents)
'''

#################################################
#                My Solution                    #
#################################################

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
c = int(input())
b = []
output = []

for i in range(n):
    b.append(int(input()))  # b(budgets)

budgets = sorted(b)  # sorted budgets

# 기본적인 condition
# 예산의 합이 선물의 금액보다 적어서는 안된다.
if sum(budgets) < c:
    # print(budgets)
    print("IMPOSSIBLE")
else:
    # if n % 2 == 1:
    remain = c
    # 1. 너 얼마나 많이 돈을 줄 수 있어?
    for i in range(len(budgets)):
        num = n - i
        if int(budgets[i]) < int(math.floor(remain / num)):
            print(budgets[i])
            remain -=budgets[i]
        elif int(budgets[i]) > int(math.floor(remain / num)):
            if i == len(budgets)-1:
                print(remain)
            else:
                apd = int(math.floor(remain / num))
                # output.append(apd)
                remain -= apd
                print(apd)


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

# print("IMPOSSIBLE")