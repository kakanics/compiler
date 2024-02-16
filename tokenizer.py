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
