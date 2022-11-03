"""
        Date: 10/18/2021
        Author: Natalio Gomes
        Problem:
        A positive whole number n>2 is prime if no number between 2 and square root of n evenly divides n.
        Write a program that accepts a value of n as input and determines if the value is prime.
        If n is not prime, your program should quit as soon as it finds a value that evenly divides n.

        The following are examples of running the program:
        Enter a number: 9
        The number 9 is not a prime number.
"""

# Create a function that determines a prime number,
# and it takes a parameter that is the number that we are going to work with.
import time
import math


def prime_number(num):
    f = time.time()
    # If the input number is greater than 2 move to the next step.
    # Since we already know that 1 and 2 are prime we want to check for larger numbers.
    if num > 2:
        # Get the integer of the square root of the inout number.
        # (Very important because for loops does not work with float datatype)
        num_sqrt = math.floor(math.sqrt(num))
        # Set the prime_num boolean to True by default
        prime_num = True
        # Loop trough entire numbers between 2 and square root of n +1
        for i in range(2, num_sqrt + 1):
            # If remainder of n is zero when we divide it for every number in the range between 2 and square root + 1,
            # it means that it is not a prime number
            if num % i == 0:
                # Set prime_num to True
                prime_num = False
        # Since originally the prime_num is TRUE. The output for this statement will be " Prime"
        if prime_num:
            print(f"The number {num} is a  prime number")
        # if prime_num is True, otherwise it is True which it means it is NOT prime
        else:
            print(f"The number {num} is not a prime number")
    # If the input number is less than 2 the program won't work.
    else:
        print("The input number has to be greater than 2.")
    l = time.time()
    print(f"Program completed in {l - f: .2f} seconds")


def check_prime(num):
    # Using While loop
    factors = 0
    i = 2
    while i <= math.floor(math.sqrt(num)):
        if n % i == 0:
            factors += 1
            # If I want to check the factors I will delete break statement.
            # We use break statement in order to make it faster.
            break
        i += 1


# Get input from the user
n = eval(input("Enter a number: "))
# If we are outputting a code from this file "hw03.py", so this file is the main script.
if __name__ == "__main__":
    # call the function and pass n as num parameter
    prime_number(n)
    check_prime(n)


