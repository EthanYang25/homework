num1 = int(input("Enther the first number:  "))
cal = input("Enther the calculator (Choose --> +, -, *, /):  ")
num2 = int(input("Enther the 2nd number:  "))
Temp = [num1, num2, cal]


def calculator(cal):
    if cal in Temp and cal == '+':
        x = 0
        x = num1+num2
        return x

    elif cal in Temp and cal == '-':
        x = 0
        x = num1-num2
        return x
    elif cal in Temp and cal == '*':
        x = 0
        x = num1 * num2
        return x
    elif cal in Temp and cal == '/':
        x = 0
        x = num1 / num2
        return x

    else:
        print("cannot calculate")


print("**********************")
answer = calculator(cal)
print("Answer:  ", answer)
print("**********************")
