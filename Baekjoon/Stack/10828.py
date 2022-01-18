import sys
num = int(sys.stdin.readline())

stack = []

for _ in range(num):
    command_arr = sys.stdin.readline().split()

    if command_arr[0] == 'push':
        stack.append(command_arr[1])
    elif command_arr[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command_arr[0] == 'size':
        print(len(stack))
    elif command_arr[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command_arr[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
