
import random
import string


class Password:
    """
    The Password class is responsible for creating password objects and generating new password
    """

    def __init__(
        self, password_length, num_of_upper_letters, num_of_spec_chars
    ) -> None:
        """
        Constructor, init password variables

        Parameters:
           * self - current working object
           * password_length - total desired password length
           * num_of_upper_letters - total desired number of uppercase letters in password
           * num_of_spec_chars - total desired number of special characters in password
        Returns:
           * None
        """
        self.password_length = password_length
        self.num_of_upper_letters = num_of_upper_letters
        self.num_of_spec_chars = num_of_spec_chars

    def validate_input(self) -> bool:
        """
        Basic user input validation

        Parameters:
           * self - current working object
        Returns:
           * boolean value of validation process. True - user input is correct, False - user input is not correct
        """
        return (
            self.password_length >= self.num_of_spec_chars + self.num_of_upper_letters
        )

    def generate_password(self) -> str:
        """
        Password generation algorithm based on user input

        Parameters:
           * self - current working object
        Returns:
           * password: string - generated password
        """
        SPECIAL_CHARS = "!@#$%^&*()_+-={}|[]\:;<>?,./"
        num_of_lower_letters = self.password_length - (
            self.num_of_spec_chars + self.num_of_upper_letters
        )

        lower_letters = [
            random.choice(string.ascii_lowercase) for _ in range(num_of_lower_letters)
        ]
        upper_letters = [
            random.choice(string.ascii_uppercase)
            for _ in range(self.num_of_upper_letters)
        ]
        spec_chars = [
            random.choice(SPECIAL_CHARS) for _ in range(self.num_of_spec_chars)
        ]

        password_list = lower_letters + upper_letters + spec_chars
        random.shuffle(password_list)
        password = "".join(password_list)

        return password


def main():
    """
    Main program execution
    """
    try:
        password_length = int(input("How long do you want your password to be? "))
        num_of_upper_letters = int(
            input("How many upper letters do you want your password to have? ")
        )
        num_of_spec_chars = int(
            input("How many special characters do you want your password to have? ")
        )
    except ValueError:
        print("All arguments should be integers")
        return
    except Exception as e:
        print(f"Unhandled exception has occured: {e}")
        return

    password = Password(
        password_length=password_length,
        num_of_upper_letters=num_of_upper_letters,
        num_of_spec_chars=num_of_spec_chars,
    )

    validated: bool = password.validate_input()
    if not validated:
        print(
            "Unable to generate password, length of password has to be higher number that number of upper + special characters:"
        )
        print(f"Password length:{password.password_length}")
        print(f"Upper letters: {password.num_of_upper_letters}")
        print(f"Special characters: {password.num_of_spec_chars}")
        return

    generated_password = password.generate_password()

    print(f"Your password: {generated_password}")


if __name__ == "__main__":
    main()
