# Make Super Computer work hard as much as possible
import numpy as np

# task의 수와 값을 입력받아 matrix를 만들어주는 함수
'''
task의 수를 입력받는다.
입력받은 task의 수만큼 행렬을 만들어준다. e.g n x 2
'''
def make_matrix(num_task): 
    # num_task = int(input())
    work_array = np.zeros((num_task, 3))

    # print(work_array)
    # input_task = []
    input_string = input(print("task명과 시작시간 종료시간을 입력하시오(띄어쓰기로 구분 할 것): ")).split(' ')
    input_string.append(int(input_string[-1]) - int(input_string[-2]))
    matrix_ = np.matrix(input_string)

    for i in range(len(work_array)-1):
        input_task = []
        input_string = input(print("task명과 시작시간 종료시간을 입력하시오(띄어쓰기로 구분 할 것): ")).split(' ')
        input_string.append(int(input_string[-1]) - int(input_string[-2]))
        # input_string = np.concatenate((input_string, len_task), axis=1)
        maked_matrix = np.matrix(input_string)
        matrix_ = np.concatenate((matrix_, maked_matrix), axis=0)
    return matrix_

num_task = int(input())

# matrix를 만들어준다.
matrix_ = make_matrix(num_task)

# sort() big task
big_task = sorted(matrix_[:, 3])

big_index = np.where(big_task[0], matrix_[:,3])

print(matrix_)
print(matrix_.shape)

print(big_inde)