import sys
import math

message = input()

decimal = ord(message)
binary = ""
# print('print decimal: ' , decimal)

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
    bianry = str(decimal // 2) + str(decimal % 2) + binary 
    decimal = 2//2
    

print(binary)
