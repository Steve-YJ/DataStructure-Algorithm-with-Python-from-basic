# print('hello world!')

# Little Hard-Coding
tasks = [
    ['A', [2, 6]],
    ['B', [9, 15]],
    ['C', [15, 20]],
    ['D', [9, 11]],
]

Import_task = [abs(i[1][0]-i[1][1]) for i in tasks]
print('tasks: ')
print(tasks)
print('index_Import_task: ', list(enumerate(Import_task)))
Index_Import_task = list(enumerate(Import_task))
# print(Index_Import_task[0][0])

from operator import itemgetter
print(sorted(Index_Import_task, key=itemgetter(1), reverse=True))
SortedIdx_Imptask = sorted(Index_Import_task, key=itemgetter(1), reverse=True)

tasks_set = tasks = [
    ['A', {2, 6}],
    ['B', {9, 15}],
    ['C', {15, 20}],
    ['D', {9, 11}],
]
print('print tasks_set')
print(tasks_set)

efficients = []
for i in range(len(tasks)):
    # print(i)
    # 전체 테스크만큼 반복(이번 예제에서는 0~3)
    
    # 가장 중요한 테스크로 초기화
    initial = SortedIdx_Imptask[i]
    print('initialization important task: ', initial)
    # efficients = []
    for j in range(i+1, len(tasks)):  # 초기화를 제외한 반복
        sum_eff = SortedIdx_Imptask[i][1]
        sum_eff_idx = str(SortedIdx_Imptask[i][0])
        if len(tasks_set[i][1] & tasks_set[j][1]) != 0:  # 가장 중요한 테스크와 다음 테스크간에 교집합이 없다면
                                                         # 테스를 하나 더 추가해준다.
            sum_eff += SortedIdx_Imptask[j][1]
            sum_eff_idx += str(", ") + str(SortedIdx_Imptask[j][0])
        else:
            pass
        efficients.append([sum_eff, sum_eff_idx])
    

print("Super efficients:")
print(efficients)

print("Super efficients: ")
print(sorted(efficients, key=itemgetter(0), reverse=True))