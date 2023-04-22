"""Main file"""

from factorial import factorial

def main():
    """Main function"""
    num = int(input("Enter a positive integer: "))
    try:
        print(f"The factorial of {num} is {factorial(num)}")
    except ValueError:
        print("The number must be >= 0")
    except TypeError:
        print("The number must be an integer")

if __name__ == "__main__":
    main()
    