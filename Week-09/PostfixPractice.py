def evaluate_postfix(expression):
    stack = []

    for token in expression.split():

        if token == 'True':
            stack.append(True)
        elif token == 'False':
            stack.append(False)
          
        elif token == 'NOT':
            a = stack.pop()
            stack.append(not a)

        else:
            b = stack.pop()
            a = stack.pop()

            if token == 'AND':
                stack.append(a and b)
            elif token == 'OR':
                stack.append(a or b)
            else:
                print("Unknown Operator: ", token)

    return stack.pop()

expr1 = "True False AND"
expr2 = "False False OR"
expr3 = "False NOT"

print("Logic 1: ", evaluate_postfix(expr1))
print("Logic 2: ", evaluate_postfix(expr2))
print("Logic 3: ", evaluate_postfix(expr3))