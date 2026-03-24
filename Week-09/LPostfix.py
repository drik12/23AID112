def evaluate_postfix(expression):
    stack = []

    for token in expression.split():

        # Boolean values
        if token == "True":
            stack.append(True)
        elif token == "False":
            stack.append(False)

        # Unary operator (NOT)
        elif token == "NOT":
            a = stack.pop()
            stack.append(not a)

        # Binary operators
        else:
            b = stack.pop()
            a = stack.pop()

            if token == "AND":
                stack.append(a and b)
            elif token == "OR":
                stack.append(a or b)
            else:
                print("Unknown operator:", token)

    return stack.pop()


# Example expressions
expr1 = "True True AND"
expr2 = "True False OR"
expr3 = "True NOT"

print("Logic 1:", evaluate_postfix(expr1))  
print("Logic 2:", evaluate_postfix(expr2))  
print("Logic 3:", evaluate_postfix(expr3))  