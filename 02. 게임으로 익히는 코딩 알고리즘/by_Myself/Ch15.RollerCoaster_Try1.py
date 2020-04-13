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

# total은 총운행수입
# sum은 운행당 수입의 합계
total = 0
for i in range(c):  # c번 운행하는 롤러코스터
    print('tern', i)
    sum = 0
    print("initialization sum: ", sum)
    count = 0
    Tqueue = []
    for i in range(len(queue)):  # loop four times
        # while sum >= l: 
        if (sum + queue[i]) < l:
            sum += queue[i]
            print('print sum: ', sum)
            count += 1    
            print('print_count: ', count)
            total += sum
            Tqueue = queue[count:] + queue[:count]
            print("Tqueue: ", Tqueue)

        elif (sum + queue[i]) == l:
            sum += queue[i]
            total += sum 
            count +=1
            for i in range(count):
                queue = queue[count:] + queue[:count]
        else:
            # queue = Tqueue
            pass
    print(sum)
print("answer")
print("total: ", total)
print("queue: ", Tqueue)