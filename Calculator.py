#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 6 13:12:51 2024

@author: Zi Hao Chen (Jary)
"""

# CALCULATOR

"""
For this project I will be making a simple calculator that does exponents, division, addition and subtraction(order
of operation: 1.exponents(^), 2.divsion(/), 3.multiplication(*), 4.addition/subtraction(+/-)) the way this calculator 
works is it does all calculaions from left to right in respects to order of operations. The expression the user inputs 
must be inputed in one line, the inputed numbers must be postive intergers only(natrual numbers). For example, input:5 + 3 + 2 ^ 2, 
input: 5 / 2 + 4 * 2 and input: 5 / 2 + 3 ^ 2 * 5 - 2. You can have as many white spaces inbetween(example: 5   / 3*4   +2) just make 
sure there is an operator between 2 positive integers. If inputed anything else, but operators and numbers you will be asked to 
input a valid expression.

example inputs for the expression:
    example 1:
    input: "3 ^ 5 ^ 2"
    output: 59'049
      The processes for exponents in this calculator is it does 3 ^ 5 which is 243 then it does 243 ^ 2 which is 59049. 
      IT DOES NOT DO 3 TO THE POWER OF 5 TO THE POWER OF 2!!!!!!
    
    example 2:
    input: "5+5/2*4^2-8"
    ans: 37
    
When you finsih putting in your expression just press enter and a statement with the ans will be outputed
"""

# FUNCTIONS


# position_check double checks if the expression is correctly organzied with operators in between numbers and returns True if it is otherwise it returns False
def position_check(listed_expression):
    bools = False

    # checks if the numbers are postioned correctly
    for i in range(0, len(listed_expression), 2):
        if not (listed_expression[i].isdigit()):
            bools = True

    # checks if the operator are postioned correctly
    for i in range(1, len(listed_expression), 2):
        if not (listed_expression[i] in operator):
            bools = True

    return bools


# update_numbers removes 2 numbers that has been calculated and replaces the calculated value. Therefore updating the expression for the next calculation proccess
def update_numbers(listed_expression, count, answer_1):
    listed_expression[count] = answer_1
    listed_expression.pop(count - 1)
    index = listed_expression.index(answer_1)
    listed_expression.pop(index + 1)

    return listed_expression


# update_numbers_with_1_operator_in_expression does the same thing as update_numbers but it is specfilcally used if the expression uses only one of the operators for the whole expression
def update_numbers_with_1_operator_in_expression(listed_expression, answer_1):
    listed_expression[1] = answer_1
    listed_expression.pop(0)
    listed_expression.pop(1)

    return listed_expression


operator = ["/", "^", "*", "+", "-"]

# asking the user to input a math expression
inputed_expression = input("\ninput a math expression: ")

# organzing the inputed math expression into a list
inputed_expression = inputed_expression.replace(" ", "")

listed_expression = list(inputed_expression)

listed_op = []

# separately organzing and detecting which part of the expression is an number/operator
for i in range(len(inputed_expression)):
    if inputed_expression[i] in operator:
        listed_op.append(inputed_expression[i])
        inputed_expression = inputed_expression.replace(inputed_expression[i], " ", 1)


listed_expression = []
inputed_expression = inputed_expression.split(" ")

# takes the two organized list of operators and numbers and organizing it into a the expression as a list
for i in range(len(listed_op)):
    if i < len(listed_op):
        listed_expression.append(inputed_expression[i])
        listed_expression.append(listed_op[i])
    if i == len(listed_op) - 1:
        listed_expression.append(inputed_expression[i + 1])

# checking if the positions of operators and numbers are correct
bools = position_check(listed_expression)

# check first if the expression inputed by the user is undefined
for i in range(len(listed_expression)):
    if i < len(listed_expression):
        if listed_expression[i] == "/" and listed_expression[i + 1] == "0":
            listed_expression = ["undefined"]
            bools = False

# while loop runs if the inputed expression is invalid, it keeps running until the user inputs something valid
# code block inside the while loop below is the same proccess from line 95 to 131
while bools or len(listed_expression) == 0:
    bools = False
    inputed_expression = input("\ninvalid input - input a math expression: ")

    inputed_expression = inputed_expression.replace(" ", "")

    listed_expression = list(inputed_expression)

    listed_op = []

    for i in range(len(inputed_expression)):
        if inputed_expression[i] in operator:
            listed_op.append(inputed_expression[i])
            inputed_expression = inputed_expression.replace(inputed_expression[i], " ", 1)

    listed_expression = []
    inputed_expression = inputed_expression.split(" ")

    for i in range(len(listed_op)):
        if i < len(listed_op):
            listed_expression.append(inputed_expression[i])
            listed_expression.append(listed_op[i])
        if i == len(listed_op) - 1:
            listed_expression.append(inputed_expression[i + 1])

    bools = position_check(listed_expression)

    for i in range(len(listed_expression)):
        if i < len(listed_expression):
            if listed_expression[i] == "/" and listed_expression[i + 1] == "0":
                listed_expression = ["undefined"]
                bools = False


# CALCULATION SECTION

# EXPONENTS

# if the expression only uses the operator "^" multiple times it will run the code block in the if statement below
if not ("+" in listed_expression) and not ("-" in listed_expression) and not ("*" in listed_expression) and not ("/" in listed_expression):

    # calculates all instances where there is "^" until there is none left
    while "^" in listed_expression:
        while len(listed_expression) > 1:
            value_1 = listed_expression[0]
            value_2 = listed_expression[2]

            # caluating the power of the number before "^" and after
            answer_1 = float(value_1) ** float(value_2)

            # updates the listed_expression
            listed_expression = update_numbers_with_1_operator_in_expression(listed_expression, answer_1)

# if the expression includes variety of different operators including "^" the code block in the else statement below will run
else:

    # calculates all instances where there is "^" until there is none left
    while "^" in listed_expression:
        count = 1
        while len(listed_expression) > count:
            symbol = listed_expression[count]
            if symbol == "^":
                value_1 = listed_expression[count - 1]
                value_2 = listed_expression[count + 1]

                # caluating the power of the number before "^" with the number after it
                answer_1 = float(value_1) ** float(value_2)

                # updates the listed_expression
                listed_expression = update_numbers(listed_expression, count, answer_1)

            count += 2

# DIVISION

# if the expression only uses the operator "/" multiple times it will run the code block in the if statement below
if not ("+" in listed_expression) and not ("-" in listed_expression) and not ("*" in listed_expression) and not ("^" in listed_expression):

    # calculates all instances where there is "/" until there is none left
    while "/" in listed_expression:
        while len(listed_expression) > 1:
            value_1 = listed_expression[0]
            value_2 = listed_expression[2]

            # dividing the number before "/" and after it
            answer_1 = float(value_1) / float(value_2)

            # updates the listed_expression
            listed_expression = update_numbers_with_1_operator_in_expression(listed_expression, answer_1)

# if the expression includes variety of different operators including "/" the code block in the else statement below will run
else:

    # calculates all instances where there is "/" until there is none left
    while "/" in listed_expression:
        count = 1
        while len(listed_expression) > count:
            symbol = listed_expression[count]
            if symbol == "/":
                value_1 = listed_expression[count - 1]
                value_2 = listed_expression[count + 1]

                # dividing the number before "/" with the number after it
                answer_1 = float(value_1) / float(value_2)

                # updates the listed_expression
                listed_expression = update_numbers(listed_expression, count, answer_1)

            count += 2

# MULTIPLICATION

# if the expression only uses the operator "*" multiple times it will run the code block in the if statement below
if not ("+" in listed_expression) and not ("-" in listed_expression) and not ("/" in listed_expression) and not ("^" in listed_expression):

    # calculates all instances where there is "*" until there is none left
    while "*" in listed_expression:
        while len(listed_expression) > 1:
            value_1 = listed_expression[0]
            value_2 = listed_expression[2]

            # multiplying the number before "*" with the number after it
            answer_1 = float(value_1) * float(value_2)

            # updates the listed_expression
            listed_expression = update_numbers_with_1_operator_in_expression(listed_expression, answer_1)


else:

    # calculates all instances where there is "*" until there is none left
    while "*" in listed_expression:
        count = 1
        while len(listed_expression) > count:
            symbol = listed_expression[count]
            if symbol == "*":
                value_1 = listed_expression[count - 1]
                value_2 = listed_expression[count + 1]

                # multiplying the number before "*" with the number after it
                answer_1 = float(value_1) * float(value_2)

                # updates the listed_expression
                listed_expression = update_numbers(listed_expression, count, answer_1)

            count += 2

# ADDITION/SUBTRACTION
# Calculates all instances of "+" and "-" from left to right from whatever there is left in the listed_expression
while "+" in listed_expression or "-" in listed_expression:
    while len(listed_expression) > 1:
        symbol = listed_expression[1]

        # addition
        if symbol == "+":
            value_1 = listed_expression[0]
            value_2 = listed_expression[2]

            # adding the number before "+" with the number after
            answer_1 = float(value_1) + float(value_2)

            # updates the list
            listed_expression = update_numbers_with_1_operator_in_expression(listed_expression, answer_1)

        # subtraction
        if symbol == "-":
            value_1 = listed_expression[0]
            value_2 = listed_expression[2]

            # subtracting the number before "-" with the number after it
            answer_1 = float(value_1) - float(value_2)

            # updates the listed_expression
            listed_expression = update_numbers_with_1_operator_in_expression(listed_expression, answer_1)


# reads the name of the user in name.txt so it can be in the statement of the final output
with open("name.txt", "r") as my_file:
    content = my_file.read()

# final returns a statement with the name you entered the the ans to the math expression
print(f"\nThe answer is: {listed_expression[0]}")
