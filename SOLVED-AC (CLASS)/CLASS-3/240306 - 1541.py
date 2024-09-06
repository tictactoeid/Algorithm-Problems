# 잃어버린 괄호
# 실버 2

calc = input()

parse = []
idx = 0
result_string = ""
for i in range(len(calc)):
    if not calc[i].isdigit():
        parse.append(int(calc[idx:i]))
        parse.append(calc[i])
        idx = i+1
parse.append(int(calc[idx:]))

isLeft = True
for x in parse:
    if x == "-":
        if isLeft:
            result_string += x
            result_string += "("
        else:
            result_string += ")"
            result_string += x
            result_string += "("
            isLeft = not isLeft
        isLeft = not isLeft
    else:
        result_string += str(x)

if not isLeft:
    result_string += ")"

#print(result_string)
print(eval(result_string))
