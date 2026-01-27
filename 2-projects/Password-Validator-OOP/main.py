import logging
from validators import PasswordValidator
from show_rules import show_rules

def menu() -> str:
    print("\nPassword Validator")
    print("1. Validate password")
    print("2. Show rules")
    print("3. Exit")
    option = input("Enter option: ")
    return option

def main() -> None:
    logging.info("Program started")

    while True:
        option = menu()

        if option == "1":
            password = input("Enter password: ")
            errors = []

            validators = [
                PasswordValidator.len_password,
                PasswordValidator.has_uppercase,
                PasswordValidator.has_lowercase,
                PasswordValidator.has_digit
            ]

            for validate in validators:
                try:
                    validate(PasswordValidator, password)
                except ValueError as e:
                    errors.append(str(e))

            if errors:
                print("\nPassword is invalid:")
                for error in errors:
                    print("-", error)
            else:
                print("\nPassword is valid")

        elif option == "2":
            logging.info("Showing rules")
            show_rules()

        elif option == "3":
            logging.info("Program finished")
            print("Goodbye")
            break

        else:
            logging.error("Invalid option")
            print("Invalid option")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()