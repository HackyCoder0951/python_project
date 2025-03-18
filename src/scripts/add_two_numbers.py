from src.modules.math import add
from src.modules.stdio import take_user_input
# from src.validations.number_validation import get_valid_number

def main():
    num1 = take_user_input("\nEnter first number: ", int)
    num2 = take_user_input("Enter second number: ", int)

    # addition of two numbers
    sum = add(num1, num2)
    if type(sum) == float or type(sum) == int:
        print("sum of two number is:", sum)
    else:
        print(sum)
