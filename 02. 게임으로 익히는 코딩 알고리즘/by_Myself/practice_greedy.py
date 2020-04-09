# Exchange Practice
# 1140원 거슬러주기

# input
# Sum of Exchange
sum_ex = input()
sum_ex = int(sum_ex)
print('sum_ex: ', sum_ex)

exchange = [0, 0, 0, 0] # 500, 100, 50, 10

# 500, 100, 50, 10

while sum_ex > 0:
    print("processing...")
    if sum_ex >= 500:
        exchange[0] += 1
        sum_ex -= 500
    elif sum_ex > 100:
        exchange[1] += 1
        sum_ex -= 100
    elif sum_ex > 50:
        exchange[2] += 1
        sum_ex -= 50
    else:
        exchange[3] += 1
        sum_ex -= 10
        
# output
print('output: ', exchange)