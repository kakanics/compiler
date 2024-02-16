from tokenizer import tokenize

print("Enter/Paste your content.")
code = ""
while True:
    try:
        line = input()
    except EOFError:
        break
    code += line
    code += '\n'


tokens = tokenize(code)
print(tokens)
