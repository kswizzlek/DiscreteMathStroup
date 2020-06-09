from gcd.gcd import *

def welcome_message():
    print("Welcome! This application will find the gcd for twon numbers")

def get_input_from_user():
    first_input = input("please enter the first number: ")
    second_input = input("please enter the second number: ")
    return first_input, second_input

def run_application():
    welcome_message()
    fn, sn = get_input_from_user()
    gcd, _, _ = get_gcd(int(fn), int(sn))

    print(f'the greatest common denominator for {fn} and {sn}:')
    print(gcd)

run_application()
