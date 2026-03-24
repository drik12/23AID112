def evaluate_prefix_logical(expression):
    stack = []
    tokens = expression.split()[::-1]

    for token in tokens:

        if token == "True":
            stack.append(True)
        elif token == "False":
            stack.append(False)

        # Unary operator
        elif token == "NOT":
            a = stack.pop()
            stack.append(not a)

        # Binary operators
        else:
            a = stack.pop()
            b = stack.pop()

            if token == "AND":
                stack.append(a and b)
            elif token == "OR":
                stack.append(a or b)
            else:
                print("Unknown operator:", token)

    return stack.pop()


# Examples
expr1 = "AND True True"
expr2 = "OR True False"
expr3 = "NOT True"

print("Logic 1:", evaluate_prefix_logical(expr1))  
print("Logic 2:", evaluate_prefix_logical(expr2))  
print("Logic 3:", evaluate_prefix_logical(expr3))  