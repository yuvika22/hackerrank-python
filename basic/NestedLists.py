# Solution to https://www.hackerrank.com/challenges/nested-list/problem


def find_second_low(scores, names_scores):
    return


if __name__ == '__main__':
    # scores = [37.21,  37.21, 37.2, 41, 39]
    # names_scores = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    scores = []
    names_scores = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        if score not in scores:
            scores.append(score)
        names_scores.append([name, score])

    names_scores.sort()
    scores.sort()

    print(scores)
    second_Lowest = -1
    if len(scores) > 1:
        second_Lowest = scores[1]

    for names in names_scores:
        if second_Lowest == names[1]:
            print(names[0])
