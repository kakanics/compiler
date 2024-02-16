import re

# This function breaks the input into tokens


def tokenize(inp):
    sol = []
    token = ""
    i = 0
    while i < len(inp):
        if inp[i] == "/" and i+1 < len(inp) and inp[i + 1] == "/":
            while i < len(inp) and inp[i] != "\n":
                i += 1
            continue
        if inp[i] == "\n":
            if token != "":
                sol.append(token)
            token = ""
            i += 1
            continue
        if inp[i] == " ":
            if token != "":
                sol.append(token)
            token = ""
        elif inp[i] in [';', '+', '-', '*', '/', '(', ')', '{', '}', '%', '!', '=', '==', '!=', '>', '<', '>=', '<=', '&&', '||']:
            if token != "":
                sol.append(token)
            sol.append(inp[i])
            token = ""
        else:
            token += inp[i]

        i += 1

    return sol

# This functions categorizes the tokens into keywords, special symbols, identifiers etc
# uses regex


def categorize(tokens):
    sol = []
    for i in tokens:
        if re.match(r';|\(|\)|\{|\}|\=', i):
            sol.append(("Special Symbol"))
        elif re.match(r"int|float|char|void|main|if|else|while|return|for|while", i):
            sol.append("Keyword")
        elif re.match(r"[a-zA-Z_][a-zA-Z0-9_]*", i):
            sol.append("Identifier")
        elif re.match(r"[0-9]+", i):
            sol.append("Number")
        elif re.match(r"==|!=|>|<|>=|<=|&&|\|\||\+|\-|\*|%", i):
            sol.append("Operator")
        elif re.match(r"pi,g", i):
            sol.append("Constant")
        else:
            return Exception("Invalid token: " + i)
    return sol
