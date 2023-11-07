problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
result = False

arithmetic_arranger(problems, result)

def arithmetic_arranger(problems, result):

    # divide the calculation
    firstline = ""
    secondline = ""
    dashline = ""
    resultline = ""

    for problem in problems:
        number1 = problem.split()[0]
        operator = problem.split()[1]
        number2 = problem.split()[2]
        #print(number1)
        #print(number2)

        # check operator
        if not (operator == "+" or operator == "-"):
            return("Error: Operator must be '+' or '-'.")

        # check if digit
        if not (number1.isdigit or number2.isdigit):
            return("Error: Numbers must only contain digits.")

        # length of numbers
        if (len(number1) > 4 or len(number2) > 4):
            return("Error: Numbers cannot be more than four digits.")

        # find longest_number
        number_list = [number1, number2]
        longest_word = max(number_list, key=len)
        i = len(longest_word)
        #print(i)

        # alignment
        upper_line = number1.rjust(i + 2)
        bottom_line = operator + number2.rjust(i + 1)
        #print(upper_line)
        #print(bottom_line)

        # if result = true
        if result == True:
            if operator == "+":
                sum = str(int(number1) + int(number2))


            else:
                sum = str(int(number1) - int(number2))


        sum = sum.rjust(i + 2)
        dash = "-" * (i)
        dash = dash.rjust(i + 2)
            #print(dash)
            #print(result)
            #print("\n")



        firstline = firstline + upper_line + "    "
        secondline = secondline + bottom_line + "    "
        dashline = dashline + dash + "    "
        resultline = resultline + sum + "    "


    print(firstline)
    print(secondline)
    print(dashline)
    print(resultline)