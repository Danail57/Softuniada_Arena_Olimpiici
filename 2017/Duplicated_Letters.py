text = input()

stack = []
operations = 0
for char in text:
    if stack and stack[-1] == char:
        stack.pop()
        operations += 1
    else:
        stack.append(char)
result = "".join(stack)
if result:
    print(result)
else:
    print("Empty String")
print(f"{operations} operations")
