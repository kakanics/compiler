from lexicalAnalyser import tokenize, categorize

print("Enter/Paste your content. Then press ctrl+z in a newline and enter")
code = ""
while True:
    try:
        line = input()
    except EOFError:
        break
    code += line
    code += '\n'


tokens = tokenize(code)
analyzed = categorize(tokens)

print(tokens)
print(analyzed)
