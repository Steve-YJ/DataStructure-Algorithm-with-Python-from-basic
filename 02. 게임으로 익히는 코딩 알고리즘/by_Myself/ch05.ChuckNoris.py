# Noris Encodding
# Input to ASCII
# ASCII to binary
# binary to unary!
# Done -20.04.07.tue-

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()
# 단일 문자 처리
'''
ord() python 내장함수
문자의 ASCII 코드 값을 돌려준다.
message=ord(message)
'''
# <Step1> binary 인코딩
# to_binary(): 10진수를 binary로 출력해주는 함수 
# ord()함수를 통해 변환한 ASCII 코드(decimal) 값을 
# binary(2진수)로 변환해준다.변환해준다
def to_binary(decimal):
    binary = ""
    
    while decimal > 0:
        remain = str(decimal % 2)
        # remain = str(remain)
        binary += remain
        decimal //= 2
    
    binary = binary[::-1]
    
    # Handling 6-bit
    if len(binary) == 6:
        binary = "0" + binary 

    return binary

# <Step2> 문자열 처리 함수
# 연속된 문자를 처리해주는 함수 구현
# 연속된 문자열을 binary로 변환한 뒤 합쳐준다.
def read_message(message):
    binary = ""
    
    for m in message:
        decimal = ord(m)
        binary += to_binary(decimal)
    return binary

binary = read_message(message)


# <Step3> Noris Encoding
# to_noris()
# binary code를 noris code로 인코딩한다
# Noris Encoding이 이 문제의 핵심 중 하나이다.하나이다
def to_noris(binary):
    # split strings
    # binary = binary.split()
    
    # split strings to characters
    binary = [char for char in binary]
    # print('split binary: ', binary)
    
    noris_codes = ""
    previous = ""
    # 
    for i in range(len(binary)):
        
        if previous == str(""):
            if binary[i] == str(1):
                previous = str(1)
                noris_codes += str(0) + " " + str(0)
            elif binary[i] == str(0):
                previous = str(0)
                noris_codes += str('00') + " " + str(0)
        
        elif binary[i] == previous:
            noris_codes += str(0)
        else:
            noris_codes += str(" ")
            if binary[i] == str(1):
                previous = str(1)
                noris_codes += str(0) + " " + str(0)
            elif binary[i] == str(0):
                previous = str(0)
                noris_codes += str('00') + " " + str(0)
            
    return noris_codes

noris_code = to_noris(binary)
print(noris_code )
