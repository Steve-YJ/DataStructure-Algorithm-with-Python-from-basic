import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

print('Insert number of temperatures:')
n = int(input())  # the number of temperatures to analyse
min_t = 5527

for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    if abs(t) == abs(min_t):
        if t > 0:
            min_t = t
    elif abs(t) < abs(min_t):
        min_t = t



# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(min_t)