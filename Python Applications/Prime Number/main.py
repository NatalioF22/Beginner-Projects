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

import math


class Lottery:

    def __init__(self, nums: list, guesses: list):
        self.nums = nums
        self.guesses = guesses

        self.score = 0

        if nums[0] == guesses[0]:
            self.score += 1
        if nums[1] == guesses[1]:
            self.score += 1
        if nums[2] == guesses[2]:
            self.score += 1
        if nums[3] == guesses[3]:
            self.score += 1

    def set_prize(self):
        if self.score == 4:
            return "You win the first prize"
        if self.score == 3:
            return "You win the second prize"
        if self.score == 2:
            return "You win the third prize"
        if self.score == 1:
            return "You win the fourth prize"
        if self.score == 0:
            return "Best luck next time"


class Grade:
    def __init__(self, midterm, final, quiz, lab):
        self.midterm = midterm
        self.final = final
        self.quiz = quiz
        self.lab = lab

    def grades_weight(self):
        self.m_weight = (self.midterm / 100) * 25
        self.f_weight = (self.final / 100) * 25
        self.q_weight = (self.quiz / 120) * 10
        self.l_weight = (self.lab / 130) * 40
        overall = self.m_weight + self.f_weight + self.q_weight + self.l_weight
        '''return f"Midterm: {self.m_weight}"
        return f"Final: {self.f_weight}"
        return f"Quiz: {self.q_weight}"
        return f"Lab Projects: {self.lab}"'''
        return f"Overall Grade is : {overall: .2f}"


'''
d1, d2, d3, d4 = eval(input("Set winning numbers: "))
w1,w2,w3,w4 = eval(input("Buy tickets numbers: "))

play = Lottery(w1, w2, w3, w4, d1, d2, d3, d4)
print(play.set_prize())
'''

w1, w2, w3, w4 = eval(input("Set Winning numbers: "))
d1, d2, d3, d4 = eval(input("Buy Ticket number: "))
set_nums = [w1, w2, w3, w4]
guessed_nums = [d1,d2,d3,d4]
obj = Lottery(set_nums, guessed_nums)
print(obj.set_prize())


class TwoNum:
    def __init__(self, lst: list, target: int):
        self.add_pairs = []
        self.sub_pairs = []
        self.even_nums = []
        self.lst = lst
        self.target = target

    def TwoSum(self):
        for i in range(len(self.lst)):
            for j in range(1, len(self.lst)):
                if self.lst[i] + self.lst[j] == self.target:
                    self.add_pairs.append((i, j))
        for pair in self.add_pairs:
            print(f"The pairs that add to {self.target} are: {pair[0] + 1} and {pair[1] + 1}")

    def TwoSub(self):
        for i in range(len(self.lst)):
            for j in range(1, len(self.lst)):
                if self.lst[i] - self.lst[j] == self.target:
                    self.sub_pairs.append((i, j))
        for pair in self.sub_pairs:
            print(f"The pairs that subtract each other to result {self.target} are: {pair[0] + 1} and {pair[1] + 1}")

    def EvenNum(self, nums):
        self.nums = nums
        self.even_nums = []
        for i in range(1, len(nums)):
            if i % 2 == 0:
                self.even_nums.append(i)
        print(f"Even numbers: {self.even_nums}")


nums = [x for x in range(1, 50)]


class Prime_Number:
    def __init__(self, n: int):
        self.n = n
        self.sqrt = math.floor(math.sqrt(self.n))
        self.prime_num = False

    def check_num(self):
        if n > 2:
            for i in range(2, self.sqrt + 1):
                if self.n % i == 0:
                    self.prime_num = True
            if self.prime_num:
                return f"The number {self.n} is not a prime number "
            else:
                return f"The number {self.n} is a prime number "
        return "The number has to be greater than 2"


if __name__ == "__main__":
    '''midterm = eval(input("Midterm grade: "))
    final = eval(input("Final Grade: "))
    quiz = eval(input("Quiz grade: "))
    lab = eval(input("Lab Grade:  "))

    grades = Grade(midterm, final, quiz, lab)
    student = grades.grades_weight()
    print(student)

    t = 2
    obj = TwoNum(nums, t)
    new_test = TwoNum(nums, t)
    new_test.EvenNum(nums)
    '''
    n = eval(input("Enter a number: "))
    n_obj = Prime_Number(n)
    print(n_obj.check_num())
