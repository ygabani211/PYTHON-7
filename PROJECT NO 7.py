# main.py
import datetime
import time
import math
import random
import uuid
import importlib
import string

SEPARATOR = "=================="

def show_main_menu():
    print("\n" + SEPARATOR)
    print("Welcome to Multi-Utility Toolkit")
    print(SEPARATOR)
    print("Choose an option:")
    print("1. Datetime and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Identifiers (UUID)")
    print("5. File Operations (custom Module)")
    print("6. Explore Module Attributes (dir())")
    print("7. Exit")
    print(SEPARATOR)

def datetime_menu():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            now = datetime.datetime.now()
            print(f"\nCurrent Date and Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
            print(SEPARATOR)
        elif choice == '2':
            try:
                d1_str = input("\nEnter the first date (YYYY-MM-DD): ")
                d2_str = input("Enter the second date (YYYY-MM-DD): ")
                d1 = datetime.datetime.strptime(d1_str, "%Y-%m-%d")
                d2 = datetime.datetime.strptime(d2_str, "%Y-%m-%d")
                diff = abs((d2 - d1).days)
                print(f"Difference: {diff} days")
                print(SEPARATOR)
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
        elif choice == '3':
            now = datetime.datetime.now()
            custom_format = input("Enter format (e.g., %d-%m-%Y %H:%M): ")
            print(f"Formatted Date: {now.strftime(custom_format)}")
        elif choice == '4':
            input("Press Enter to start stopwatch...")
            start_time = time.time()
            input("Press Enter to stop...")
            elapsed = time.time() - start_time
            print(f"Elapsed time: {elapsed:.2f} seconds")
        elif choice == '5':
            try:
                secs = int(input("Enter countdown time in seconds: "))
                print("Countdown started...")
                for i in range(secs, 0, -1):
                    print(f"{i}...", end=" ", flush=True)
                    time.sleep(1)
                print("\nTime's up!")
            except ValueError:
                print("Please enter a valid integer.")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Try again.")

def math_menu():
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                num = int(input("\nEnter a number: "))
                print(f"Factorial: {math.factorial(num)}")
                print(SEPARATOR)
            except ValueError:
                print("Please enter a positive integer.")
        elif choice == '2':
            try:
                p = float(input("\nEnter principal amount: "))
                r = float(input("Enter rate of interest (in %): "))
                t = float(input("Enter time (in years): "))
                amount = p * math.pow((1 + r/100), t)
                print(f"Compound Interest: {amount:.2f}")
                print(SEPARATOR)
            except ValueError:
                print("Invalid input.")
        elif choice == '3':
            angle = float(input("Enter angle in degrees: "))
            rad = math.radians(angle)
            print(f"Sin: {math.sin(rad):.4f}, Cos: {math.cos(rad):.4f}, Tan: {math.tan(rad):.4f}")
        elif choice == '4':
            print("Area of Circle: 3.14 * r^2")
            radius = float(input("Enter radius: "))
            print(f"Area: {math.pi * math.pow(radius, 2):.2f}")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")

def random_menu():
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            print(f"Random Number: {random.randint(1, 100)}")
        elif choice == '2':
            rand_list = [random.randint(1, 100) for _ in range(5)]
            print(f"Random List: {rand_list}")
        elif choice == '3':
            try:
                length = int(input("\nEnter password length: "))
                chars = string.ascii_letters + string.digits + string.punctuation
                password = ''.join(random.choice(chars) for _ in range(length))
                print(f"Generated Password: {password}")
                print(SEPARATOR)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            otp = random.randint(100000, 999999)
            print(f"Generated OTP: {otp}")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")

def uuid_menu():
    print("\nGenerate Unique Identifiers:")
    print(f"Generated UUID: {uuid.uuid4()}")
    print(SEPARATOR)

def file_menu():
    while True:
        print("\nFile Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            filename = input("\nEnter file name: ")
            file_ops.create_file(filename)
            print(SEPARATOR)
        elif choice == '2':
            filename = input("\nEnter file name: ")
            data = input("Enter data to write: ")
            file_ops.write_file(filename, data)
            print(SEPARATOR)
        elif choice == '3':
            filename = input("\nEnter file name: ")
            file_ops.read_file(filename)
            print(SEPARATOR)
        elif choice == '4':
            filename = input("\nEnter file name: ")
            data = input("Enter data to append: ")
            file_ops.append_file(filename, data)
            print(SEPARATOR)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")

def explore_module_menu():
    print("\nExplore Module Attributes:")
    module_name = input("Enter module name to explore: ")
    try:
        module = importlib.import_module(module_name)
        attributes = dir(module)
        print(f"Available Attributes in {module_name} module:")
        print(attributes)
        print(SEPARATOR)
    except ImportError:
        print(f"Error: Module '{module_name}' not found.")
        print(SEPARATOR)

def main():
    while True:
        show_main_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            datetime_menu()
        elif choice == '2':
            math_menu()
        elif choice == '3':
            random_menu()
        elif choice == '4':
            uuid_menu()
        elif choice == '5':
            file_menu()
        elif choice == '6':
            explore_module_menu()
        elif choice == '7':
            print("\n" + SEPARATOR)
            print("Thank you for using the Multi-Utility Toolkit!")
            print(SEPARATOR)
            break
        else:
            print("Invalid choice. Please select from 1 to 7.")

if __name__ == "__main__":
    main()