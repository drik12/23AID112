def evaluate_prefix(expression):
    stack = []

    tokens = expression.split()[::-1]

    for token in tokens:
        if token == 'True':
            stack.append(True)
        elif token == 'False':
            stack.append(False)

        elif token == 'NOT':
            a = stack.pop()
            stack.append(not a)

        else:
            a = stack.pop()
            b = stack.pop()

            if token == 'AND':
                stack.append(a and b)
            elif token == 'OR':
                stack.append(a or b)
            else:
                print("Unknown Operator: ", token)

    return stack.pop()

expr1 = "AND True False" 
expr2 = "OR True True"
expr3 = "NOT False"

print("Logic 1: ", evaluate_prefix(expr1))
print("Logic 2: ", evaluate_prefix(expr2))
print("Logic 3: ", evaluate_prefix(expr3))

