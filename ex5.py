# A simple Python program

def greet_user(name, age):
    print(f"Hello, {name}!")
    print(f"You are {age} years old.")

def main():
    # Get user's name and age
    name = input("Enter your name: ")
    age = input("Enter your age: ")

    # Validate that age is a number
    if not age.isdigit():
        print("Please enter a valid age.")
        return

    age = int(age)
    greet_user(name, age)

if __name__ == "__main__":
    main()
