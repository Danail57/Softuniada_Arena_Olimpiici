text = input()
stack = []
closed_pairs = 0
is_valid = True

pairs = {")": "(", "]": "[", "}": "{"}

for char in text:
    if char in "([{":
        stack.append(char)
    elif char in pairs:
        if not stack or stack[-1] != pairs[char]:
            is_valid = False
            break
        else:
            stack.pop()
            closed_pairs += 1

if is_valid and not stack:
    print("Valid")
    print(f"{closed_pairs} pairs closed")
else:
    print("Invalid")
    print("0 pairs closed")
