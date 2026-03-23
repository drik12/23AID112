def precedence(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    elif op == '^':
        return 3
    return 0


def infix_to_postfix(expression):
    stack = []
    output = ""

    for char in expression:
        
        # If operand → add to output
        if char.isalnum():
            output += char

        # If '(' → push to stack
        elif char == '(':
            stack.append(char)

        # If ')' → pop until '('
        elif char == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()

        # If operator
        else:
            while (stack and precedence(stack[-1]) >= precedence(char)):
                output += stack.pop()
            stack.append(char)

    # Pop remaining operators
    while stack:
        output += stack.pop()

    return output


# Example
expr = "A+B*(C-D)"
result = infix_to_postfix(expr)

print("Infix Expression :", expr)
print("Postfix Expression :", result)