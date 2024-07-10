import random
import string

def generate_password(length):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation
    all_chars = lowercase + uppercase + digits + special_chars
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            print("Invalid length. Please enter a positive integer.")
            return

        password = generate_password(length)
        print(f"Generated password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

if __name__ == "__main__":
    main()