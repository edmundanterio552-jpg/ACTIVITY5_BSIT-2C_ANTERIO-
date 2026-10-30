def is_balanced(expression):
    stack = []
    matching_open = {')': '(', ']': '[', '}': '{'}

    for character in expression:
        if character in "([{":
            stack.append(character)
        elif character in ")]}":
            if not stack or stack.pop() != matching_open[character]:
                return False

    return len(stack) == 0


if __name__ == "__main__":
    expression = input("Enter an expression: ")
    if is_balanced(expression):
        print("The expression is balanced.")
    else:
        print("The expression is not balanced.")
