# 20.04.13.mon
# Roller Coaster do it by myself

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l, c, n = [int(i) for i in input().split()]
# print(l, c, n)


queue = [int(input())  for i in range(n)]
print('input queue: ', queue)

# sum
# sum = 0
total = 0
for i in range(c):
    sum = 0
    # queue_0 = queue[0]
    for i in range(len(queue)):  # loop four times
        if (sum + queue[i]) < l:
            sum += queue[i]
            total += sum
            # print('print sum:, ', sum)    
        elif (sum + queue[i]) == l:
            sum += queue[i]
            total += sum
            # print('total(sum+queue): ', total)
            # same = queue[i]
            queue_0 = queue[0]
            # print('sum == l: ', sum) 
            for j in range(len(queue)):
                if j == (len(queue)-1):
                    queue[j] = queue_0
                else:
                    queue[j] = queue[j+1]
            # print(queue)
            # print(i)
        elif (sum + queue[i]) > l:
            # print('sum > l: ', sum)
            queue_0 = queue[0]
            # sum += queue[i]
            # if sum == l:
                # queue[i] = queue[i+1]
            for j in range(len(queue)):
                if j == (len(queue)-1):
                    queue[j] = queue_0
                else:
                    queue[j] = queue[j+1]
            # print(queue)
            # print(i)
        # print('sum_one-circle: ', sum)
# print(sum)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)

print("answer")
print("total: ", total)