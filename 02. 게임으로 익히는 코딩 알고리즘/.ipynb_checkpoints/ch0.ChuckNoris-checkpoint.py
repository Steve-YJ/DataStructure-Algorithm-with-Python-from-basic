import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()
# C
# decimal = ord(message)

## CC
decimal_list = []

for i in message:
    decimal_list.append(ord(i))
    
# print(decimal_list)

def to_binary(decimal):
    binary = ""
    
    while decimal // 2 > 0:
        remain = str(decimal % 2)
        binary = remain + binary
        decimal //= 2

        if decimal == 2:
            fin = str(decimal // 2)
            remain = str(decimal % 2)
            binary = fin + remain + binary
            decimal = 2//2
            
        if len(binary) == 6:
            binary = "0" + binary
            
    return binary
    
# decimal list's element to binary
binary_list = []
for i in decimal_list:
    binary_list.append(to_binary(i))
    
# binary = to_binary(decimal) 

# concatenate binarys
binary = ""
for i in range(len(decimal_list)):
    binary += binary_list[i]

def to_noris(binary):
    binary = list(binary)
    previous = ""
    current = ""
    noris = ""
    
    if binary[0] == str(0):  # binary[0]
        noris += "00 0"
        previous = "0"
    elif binary[0] == str(1):
        noris += "0 0"
        previous = "1"  
  
    for i in range(1, len(binary)):
        previous = previous
        if binary[i] == previous:  # compare
            noris += "0"
        elif binary[i] != previous:
            noris += " "
            if binary[i] == str(0):
                noris += "00 0"
                previous = "0"
            elif binary[i] == str(1):
                noris += "0 0"
                previous = "1"
    return noris
    
    
noris = to_noris(binary)
print(noris)
    
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)