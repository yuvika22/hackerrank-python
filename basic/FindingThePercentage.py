# Solution to https://www.hackerrank.com/challenges/finding-the-percentage/problem?h_r=next-challenge&h_v=zen

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    # print(student_marks)

n = student_marks[query_name]

# print([n])

sum = 0

for marks in n:
    sum = sum + marks
print("%1.2f" % (sum/len(n)))
