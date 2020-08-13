import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# message = input()
message = "C" 
decimal = ord(message)
print(decimal)
binary = ""
# print('print decimal: ' , decimal)

# Step1. Convert Character to binary
# char to binary
while decimal // 2 > 0:
    print('start decimal: ', decimal)
    remain = str(decimal % 2)
    print('remain:', remain)
    binary = remain + binary
    print('binary:', binary)
    decimal //= 2
    print('decimal: ', decimal)
    print('='*20)

    if decimal == 2:
        print('decimal==2?:', decimal)
        # binary = "10"+binary
        fin = str(decimal // 2)
        remain = str(decimal % 2)
        binary = fin + remain + binary
        print('final_binary: ', binary)
        decimal = 2//2
    
print('binary: ', binary)
print(type(binary[0]))
# print(type(str(binary[0])))
# print(len(binary))


# Step2. binary to Noris code
# encoding

binary = list(binary)
print(binary)
# 변수의 초기화를 잘 시켜놓자.
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
    
print('pirnt noris code: ', noris)
    