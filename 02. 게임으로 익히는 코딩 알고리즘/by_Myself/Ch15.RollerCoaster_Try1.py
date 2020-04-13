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
    print('tern', i)
    sum = 0
    print("initialization sum: ", sum)
    count = 0
    Tqueue = queue
    for i in range(len(Tqueue)):  # loop four times
        # while sum >= l: 
        if (sum + Tqueue[i]) < l:
            sum += Tqueue[i]
            print('print sum: ', sum)
            count += 1    
            print('print_count: ', count)
            total += sum
            Tqueue = Tqueue[count:] + Tqueue[:count]
            print("Tqueue: ", Tqueue)

        elif (sum + Tqueue[i]) == l:
            sum += Tqueue[i]
            total += sum 
            count +=1
            for i in range(count):
                Tqueue = Tqueue[count:] + Tqueue[:count]
        else:
            break
    print(Tqueue)
print("answer")
print("total: ", total)
print("Tqueue: ", Tqueue)