# 앞서 구현한 최소 개수 동전 거스름돈 문제를 다른 방법으로 구현해보자

sum_ex = int(input())  # 정수 단위로 잔돈의 합계를 입력받는다
                       # e.g 1140원

# exchange 
# 동전 각각의 개수와 최소 거스름 돈의 수를 출력하라

exchange = [0, 0, 0, 0]

while sum_ex > 0:
    if sum_ex >= 500:
        exchange[0] +=1
        sum_ex -= 500
    elif sum_ex >= 100 :
        exchange[1] +=1
        sum_ex -= 100
    elif sum_ex >= 50:
        exchange[2] +=1
        sum_ex -= 50
    else:
        exchange[3] +=1
        sum_ex -= 10

print('output: ', exchange)
print('total_num_coin: ', sum(exchange))