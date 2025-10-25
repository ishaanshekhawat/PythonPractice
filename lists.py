if __name__ == '__main__':
    N = int(input())

m = []
f = []



for i in range(len(m)):
    if m[i][0] == 'insert':
        f.insert(int(m[i][1]), int(m[i][2]))
    elif m[i][0] == 'print':
        print(f)
    elif m[i][0] == 'remove':
        f.remove(int(m[i][1]))
    elif m[i][0] == 'append':
        f.append(int(m[i][1]))
    elif m[i][0] == 'sort':
        f.sort()
    elif m[i][0] == 'pop':
        f.pop()
    elif m[i][0] == 'reverse':
        f.reverse()
    else:
        print("Please enter valid operations!")



# for _ in range(N):
#         cmd, *args = input().split()
#         args = list(map(int, args))  # convert all arguments to int

#         if cmd == "insert":
#             lst.insert(args[0], args[1])
#         elif cmd == "print":
#             print(lst)
#         elif cmd == "remove":
#             lst.remove(args[0])
#         elif cmd == "append":
#             lst.append(args[0])
#         elif cmd == "sort":
#             lst.sort()
#         elif cmd == "pop":
#             lst.pop()
#         elif cmd == "reverse":
#             lst.reverse()