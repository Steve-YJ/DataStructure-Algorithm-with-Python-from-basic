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
    for i in range(len(queue)):  # loop four times
        while sum >= l:
            break
        else:
            if (sum + queue[i]) < l:
                sum += queue[i]
                print('print sum: ', sum)
                count += 1    
                print('print_count: ', count)
                total += sum
                
            elif (sum + queue[i]) == l:
                sum += queue[i]
                total += sum 
                count +=1
                for i in range(count):
                    queue = queue[count:] + queue[:count]
                
            elif (sum + queue[i]) > l:
                for i in range(count):
                    queue = queue[count:] + queue[:count]
         
    print('After one-circle: ',total)
    print(queue)
# print(sum)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)

print("answer")
print("total: ", total)