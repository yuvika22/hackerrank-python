# Solution to https://www.hackerrank.com/challenges/list-comprehensions/
# Code completed on 12/23/2020

def myfunction(x, y, z, n):
    myarray = []
    for i in range(0, x):
        for j in range(0, y):
            for k in range(0, z):
                if i + j + k != n:
                    myarray.append([i, j, k])
    print(myarray)


if __name__ == '__main__':
    x = int(input()) + 1
    y = int(input()) + 1
    z = int(input()) + 1
    n = int(input())
    myfunction(x, y, z, n)
