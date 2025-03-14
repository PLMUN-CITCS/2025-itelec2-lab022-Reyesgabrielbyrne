def display_menu() -> None:
    """
    Displays the program's menu options to the user.
    """
    print("\nMenu:")
    print("1. Greet User")
    print("2. Check Even/Odd")
    print("3. Exit")

def get_integer_input(prompt: str) -> int:
    """
    Prompts the user to enter an integer and validates input.

    Args:
        prompt (str): The message to display when asking for input.

    Returns:
        int: The validated integer input.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def check_even_odd(number: int) -> str:
    """
    Determines if a given number is even or odd.

    Args:
        number (int): The integer to check.

    Returns:
        str: A formatted message indicating whether the number is even or odd.
    """
    if number % 2 == 0:
        return f"{number} is an Even number."
    return f"{number} is an Odd number."

def greet_user() -> None:
    """
    Prints a greeting message.
    """
    print("Hello! Welcome!")

def even_odd_checker_action() -> None:
    """
    Handles the logic for checking if a number is even or odd.
    Gets user input and displays the result.
    """
    number = get_integer_input("Enter an integer: ")
    print(check_even_odd(number))

def handle_menu_choice(choice: int) -> bool:
    """
    Executes the corresponding action based on the user's menu choice.

    Args:
        choice (int): The menu option selected by the user.

    Returns:
        bool: True if the user chooses to exit, False otherwise.
    """
    if choice == 1:
        greet_user()
    elif choice == 2:
        even_odd_checker_action()
    elif choice == 3:
        print("Exiting program. Goodbye!")
        return True  # Signal to exit the program loop
    else:
        print("Invalid choice! Please enter a number between 1 and 3.")
    return False  # Continue the loop

def main():
    """
    The main function to run the menu-driven program.
    """
    while True:
        display_menu()
        choice = get_integer_input("Enter your choice (1-3): ")
        if handle_menu_choice(choice):
            break  # Exit the loop if the user chooses option 3

# Run the main function if the script is executed
if __name__ == "__main__":
    main()