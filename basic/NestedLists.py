# Solution to https://www.hackerrank.com/challenges/nested-list/problem


def find_second_low(scores, names_scores):
    return


if __name__ == '__main__':
    scores = [37.21,  37.21, 37.2, 41, 39]
    names_scores = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     scores.append([score])
    #     names_scores.append([score, name])

    scores.sort()
    names_scores.sort()

    second_low = scores[1]

    for student in names_scores:
        if student[1] == second_low:
            print("{}".format(student[0]))


