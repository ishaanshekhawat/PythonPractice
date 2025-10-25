if __name__ == '__main__':
    # Read an integer N, i.e., the number of commands to be executed
    N = int(input())

m = []  # List to store all commands entered by the user
f = []  # The main list that will be modified according to the commands

# Loop through all commands in the list 'm'
for i in range(len(m)):
    # Each element in 'm' is expected to be a list like ['insert', '0', '5']
    if m[i][0] == 'insert':
        # Insert the element at a specific position
        f.insert(int(m[i][1]), int(m[i][2]))

    elif m[i][0] == 'print':
        # Print the current state of the list
        print(f)

    elif m[i][0] == 'remove':
        # Remove the first occurrence of a specific value
        f.remove(int(m[i][1]))

    elif m[i][0] == 'append':
        # Add an element to the end of the list
        f.append(int(m[i][1]))

    elif m[i][0] == 'sort':
        # Sort the list in ascending order
        f.sort()

    elif m[i][0] == 'pop':
        # Remove the last element from the list
        f.pop()

    elif m[i][0] == 'reverse':
        # Reverse the order of the elements in the list
        f.reverse()

    else:
        # Handle invalid commands
        print("Please enter valid operations!")



# Alternative Solution below ----------------------------------------

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
