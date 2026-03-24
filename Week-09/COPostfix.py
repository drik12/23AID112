def evaluate_postfix(expression):
    stack = []

    for token in expression.split():
        if token.isdigit():
            stack.append(int(token)) 
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '==':
                stack.append(a == b)
            elif token == '<':
                stack.append(a < b)
            elif token == '>':
                stack.append(a > b)
            else:
                print("Unknown Operator: ", token)

    return stack.pop()

expr1 = "10 10 =="
expr2 = "40 30 <"
expr3 = "35 34 >"

print("Comp 1: ", evaluate_postfix(expr1))
print("Comp 2: ", evaluate_postfix(expr2))
print("Comp 3: ", evaluate_postfix(expr3))