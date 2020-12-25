# Solution https://www.hackerrank.com/challenges/python-lists/problem
if __name__ == '__main__':
    n = int(input())
    l = []
    for _ in range(n):
        function, *param_input = input().split()
        param_list = list(map(int, param_input))
        # print(function, param_list)
        if function == "insert":
            l.insert(param_list[0], param_list[1])
        elif function == "print":
            print(l)
        elif function == "remove":
            l.remove(param_list[0])
        elif function == "append":
            l.append(param_list[0])
        elif function == "sort":
            l.sort()
        elif function == "reverse":
            l.reverse()
        elif function == "pop":
            l.pop()
