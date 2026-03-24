def evaluate_prefix_comparison(expression):
    stack = []
    tokens = expression.split()[::-1]

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            a = stack.pop()
            b = stack.pop()

            if token == '==':
                stack.append(a == b)
            elif token == '>':
                stack.append(a > b)
            elif token == '<':
                stack.append(a < b)
            else:
                print("Unknown operator:", token)

    return stack.pop()


# Examples
expr1 = "== 5 5"
expr2 = "> 10 3"
expr3 = "< 2 8"

print("Comp 1:", evaluate_prefix_comparison(expr1))  
print("Comp 2:", evaluate_prefix_comparison(expr2))  
print("Comp 3:", evaluate_prefix_comparison(expr3))  