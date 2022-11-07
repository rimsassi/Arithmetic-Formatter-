def arithmetic_arranger(list_problems,cond = False):
    nb_problems = len(list_problems)
    operand1 = []
    operand2 = []
    operator_operand2 = []
    operator = []
    result = []
    for value in list_problems:
        listcheck = value.split()
        operand1.append(listcheck[0])
        operand2.append(listcheck[2])
        operator_operand2.append(listcheck[1] +" "+ listcheck[2])
        operator.append(listcheck[1])

    newlistcheck = operand1 + operand2
    checkop = all(((ele == "+") or (ele == "-")) for ele in operator)
    checkdigits = all(ele.isdigit() for ele in newlistcheck)

    checklen = False
    for ele in newlistcheck:
        if len(ele) > 4:
            checklen = True

    dashes = []
    for i in range(0,nb_problems):
        try:
            if operator[i] == "+":
                res = str(int(operand1[i]) + int(operand2[i]))
            else:
                res = str(int(operand1[i]) - int(operand2[i]))
        except :
            res = ""

        result.append(res)

        if len(res) == 1:
            dashes.append("---")
        elif len(res) == 2:
            dashes.append("----")
        elif len(res) == 3:
            dashes.append("-----")
        else:
            dashes.append("------")

    x = len(max(dashes, key=len)) 

    y = len(dashes)

    for i in range(0,y):
        operand1.append(operand1[i].rjust(x))
        operator_operand2.append(operator_operand2[i].rjust(x))
        dashes.append(dashes[i].rjust(x))
        result.append(result[i].rjust(x))

    start = int(len(operand1)/2)

    operand1 = operand1[start:]
    operator_operand2 = operator_operand2[start:]
    dashes = dashes[start:]
    result = result[start:]

    for i in range(1,y+3,2):
        operand1.insert(i, "    ")
        operator_operand2.insert(i, "    ")
        dashes.insert(i, "    ")
        result.insert(i, "    ")

    line = ''.join(str(e) for e in operand1) + "\n" + ''.join(str(e) for e in operator_operand2) + "\n" + ''.join(str(e) for e in dashes)


    if nb_problems > 5:
        return "Error: Too many problems"
    elif checkop == False:
        return "Error: Operator must be '+' or '-'."
    elif checkdigits == False:
        return "Error: Numbers must only contain digits."
    elif checklen == True:
        return "Error: Numbers cannot be more than four digits."
    else:
        if cond == False:
            return line
        elif cond == True:
            line = line + "\n" + ''.join(str(e) for e in result)
            return line