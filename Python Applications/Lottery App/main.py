"""
    Comp 151 – Computer Science I (Fall 2021)
    Homework 02
    (20 points)

    Due Date: Friday, Oct 08

    Problem
    Write a program to simulate the lottery game. The program should firstly prompt for four single-digit winning
    numbers and then prompt for four single-digit lottery numbers. Each digit in the number is in the range between 0~9.
    The program should determine which prize the user wins according to the following rule:
    • The user wins the first prize if all of the input numbers and the lottery numbers match in exact order.
    • The user wins the second prize if any three of the input numbers and the lottery numbers match in exact order.
    • The user wins the third prize if any two of the input numbers and the lottery numbers match in exact order.
    • The user wins the fourth prize if any one of the input numbers and the lottery numbers matches in exact order.

"""


def lottery():
    #First we set the winning numbers:
    d1, d2, d3, d4 = eval(input("Set four winning numbers (d1, d2, d3, d4): "))
    #Second we prompt the user to set their lottery numbers:
    w1, w2, w3, w4 = eval(input("Buy four lottery numbers (d1, d2, d3, d4): "))
    # We set the inital value of prize_num to 0
    prize_num = 0
    # As we bougth tickets macth the set numbers: we update the value of prize_num to 1
    if d1 == w1:
        prize_num +=1
    if d2 ==w2:
        prize_num += 1
    if d3 == w3:
        prize_num += 1
    if d4 == w4:
        prize_num += 1

    #Finally we determine the first, second, third, and fourth prize according to matched numbers
    if prize_num == 4:
        print("You won the FIRST price!!")
    elif prize_num == 3:
        print("You won the SECOND price!!")
    elif prize_num == 2:
        print("You won the THIRD price!!")
    elif prize_num == 1:
        print("You won the FOURTH price!!")
    else:
        print("Best Luck next time!")

if __name__ == "__main__":
    lottery()











