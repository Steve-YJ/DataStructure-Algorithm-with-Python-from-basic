# 학생들의 성적을 취합해서 평균을 구해주는 프로그램
# 배열을 사용한 버전
# 성적을 입력받는다.

number_of_students = 30
student_scores = []
total_sum = 0

for i in range(number_of_students):
    student_scores.append(int(input()))
    total_sum += student_scores[i]

average = total_sum / number_of_students
print("sum = %d, average= %d" % (total_sum, average))
