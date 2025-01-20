from random import randint, choice
from string import ascii_lowercase, ascii_uppercase, punctuation, digits


def help():
    print("\n  📖 Available commands:")
    print("  🆘 help - Show this help message")
    print("  🔑 get  - Generate a random password")
    print("  🚪 exit - Exit the program\n")


class ValidatorLength:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    
    def verification(self, instance, value):
        if not isinstance(value, str):
            print('\nError: Value must be a string. Try again 😔', end='\n\n')
        elif not value.isdigit():
            print('\nError: The string must contain only numbers. Try again 😔', end='\n\n')
        elif self.name == '_min_length' and int(value) < 8:
            print('\nError: Password length must be more than 8 characters. Try again 😔', end='\n\n')
        elif self.name == '_max_length' and instance.min_length > int(value):
            print('\nError: The maximum length must be greater than the minimum. Try again 😔', end='\n\n')
        elif self.name == '_max_length' and int(value) > 100:
            print('\nError: The password length should not exceed 100 characters. Try again 😔', end='\n\n')
        else:
            return True
        return False
    
    def __set__(self, instance, value):
        if not self.verification(instance, value):
            raise ValueError
        setattr(instance, self.name, int(value))
        

class RandomPassword:
    min_length = ValidatorLength()
    max_length = ValidatorLength()

    def __init__(self):
        self.psw_chars = (ascii_lowercase, ascii_uppercase, digits, punctuation)
        self.set_password_length()

    def set_password_length(self):
        if input('Use fixed password length (y/n): ') == 'y':
            self._set_fixed_length()
        else:
            self._set_min_max_length()

    def _set_fixed_length(self):
        while True:
            length = input('Enter password length (min 8 characters): ')
            try:
                self.min_length = length
                self.max_length = length
                break
            except ValueError:
                continue

    def _set_min_max_length(self):
        while True:
            min_length = input('Enter the minimum password length (min 8 characters): ')
            try:
                self.min_length = min_length
                break
            except ValueError:
                continue

        while True:
            max_length = input('Enter the maximum password length (max 100 characters): ')
            try:
                self.max_length = max_length
                break
            except ValueError:
                continue

    def __call__(self, *args, **kwds):
        password = ''
        for _ in range(randint(self.min_length, self.max_length)):
            password += choice(choice(self.psw_chars))
        return password
    

def main():
    print("Hello 🙋")
    commands = ('help', 'get', 'exit')

    while True:
        inp = input(f'Enter the command {commands}: ')
        if inp not in commands:
            print('\nError: the command not recognized. Try again 😔', end='\n\n')
            continue

        elif inp == 'help':
            help()

        elif inp == 'get':
            while not (count := input(f"Enter the required number of passwords: ")).isdigit() or count == '0':
                print('\nError: quantity must be a number from 0. Try again 😔', end='\n\n')

            random_password = RandomPassword()

            print()
            for _ in range(int(count)):
                print(random_password())
            print()

        elif inp == 'exit':
            break 
        
    print("Good luck 😉")

if __name__ == "__main__":
    main()