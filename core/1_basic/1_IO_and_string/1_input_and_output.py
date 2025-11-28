def read_input(prompt: str = "Enter your name: ") -> str:
    """
    Read input from the keyboard with the built-in function input()
    """
    user_input = input(prompt)
    return user_input


def run_exercise1():
    name = read_input("Enter your name: ")
    print(f"Hello, {name}!")


def convert_input_to_integer() -> int:
    """
    Convert input to an integer
    """
    return int(read_input("Enter your age: "))


def run_exercise2():
    age = convert_input_to_integer()
    age = age + 50
    print(f"After 50 years, you will be {age} years old.")


def run_exercise3() -> None:
    """
    Print arguments with a separator and an end character
    """
    age = convert_input_to_integer()
    age = age + 50
    print("you will be", age, "in 50 years")
    print("you will be", age, "in 50 years", end="\n\n\n")
    print("you will be", age, "in 50 years", sep="-")
    print("you will be", age, "in 50 years", sep="-", end=None)


def main():
    # run_exercise1()
    # run_exercise2()
    run_exercise3()


if __name__ == "__main__":
    main()
