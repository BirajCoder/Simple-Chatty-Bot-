def greet(bot_name, birth_year):
    print(f'Hello! My name is {bot_name}.')
    print(f'I was created in {birth_year}.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print(f'What a great name you have,  {name} !')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print(f"Your age is {str(age)} ; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    print("""1. Why do we use methods?
    1. To repeat a statement multiple times.
    2. To decompose a program into several small subroutines.
    3. To determine the execution time of a program.
    4. To interrupt the execution of a program.""")
    n = int(input())
    while n != 2:
        print("Please, try again.")
        n = int(input())
    print('Next question:')
    print("""2. Which operator has higher precedence in the following list?
    1. % (Modulus)
    2. & (BitWise AND)
    3. ** (Exponent)
    4. > (Comparison)
    """)
    n = int(input())
    while n != 3:
        print("Please, try again.")
        n = int(input())
    print('Next question:')
    print("""3. What is the output of the following code:
    ---------------------------------------------
        salary = 8000
        
        def printSalary():
          salary = 12000
          print("Salary:", salary)
          
        printSalary()
        print("Salary:", salary)
    ---------------------------------------------
    1. Salary: 12000 Salary: 8000
    2. Salary: 8000 Salary: 12000
    3. The program failed with errors
    """)
    n = int(input())
    while n != 1:
        print("Please, try again.")
        n = int(input())
    print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


greet('Sova', '2000')
remind_name()
guess_age()
count()
test()
end()
