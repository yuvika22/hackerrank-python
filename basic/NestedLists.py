# Solution to https://www.hackerrank.com/challenges/nested-list/problem


def find_second_low(scores, names_scores):
    return


if __name__ == '__main__':
      scores = [['c', 4.0], ['a', 2.0], ['b', 3.0], ['d', 5.0], ['f', 1.0], ['g', 2.0]]

    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append([name, score])
        names_scores.append([score, name])

        scores.sort()
        names_scores.sort()

    print(scores)

