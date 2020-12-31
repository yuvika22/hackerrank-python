if __name__ == '__main__':
    n = int(input())
    l = []

    for _ in range (n):
        # arr = (int, input().split())
        arr = (input())
        #         name, *line = input().split()
        l.append(arr)

    l.sort()
    l = list(dict.fromkeys(l))
    print(l)
















