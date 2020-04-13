import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # number of participaints 참가자의 수
p = int(input())  # present 가격
b = []            # budgets 참가자별 예산
output = []

for i in range(n):
    b.append(int(input()))  # b(budgets)

# 오름차순으로 예산 정렬
budgets = sorted(b)  # sorted budgets
# print(budgets)
# 기존 방법
'''
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
'''

# Update -20.04.13.mon. pm12:47-
if sum(budgets) < p:
    print("IMPOSSIBLE")
else:
    price = p
    num = n
    for i in range(len(budgets)):
        mean_price = math.floor(price / num)  # mean_price
        # print("mean_price: ", mean_price)
        if budgets[i] < mean_price:
            print(budgets[i])
            price -= budgets[i]
            num  -=1
        elif budgets[i] > mean_price:
            print(mean_price)
            price -= mean_price
            num -= 1
        elif i == (len(budgets)-1):
            print(price)
       
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

# print("IMPOSSIBLE")