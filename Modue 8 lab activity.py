#Idris Awodeji
#8.21.2024

#Problem 1
def check_equality():
    # Takes two inputs from the user
    input1 = input("Enter the first number: ")
    input2 = input("Enter the second number: ")
    
    # Compares equality of inputs print the result
    if input1 == input2:
        print("The two inputs are equal.")
    else:
        print("The two inputs are not equal.")

# Example
check_equality()


#Problem 2
def check_sum():
    # Takes two inputs from the user and convert them to integers
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    
    # Calculate the sum of the two numbers
    total = number1 + number2
    
    # Compares the sum to 10 and print the result
    if total > 10:
        print("The sum is greater than 10.")
    elif total < 10:
        print("The sum is less than 10.")
    else:
        print("The sum is equal to 10.")

# Example
check_sum()


#Problem 3
def check_forfive(user_list):
    # Checks if 5 is in the list
    if 5 in user_list:
        print("The value 5 is in the list.")
    else:
        print("The value 5 is not in the list.")

# Example
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
check_forfive(sample_list)


#Problem 4
def leap_year(year):
    """Returns True if the year is a leap year, False otherwise."""
    if year % 4 == 0:  # Checks if year is divisible by 4
        if year % 100 == 0:  # If divisible by 100, check further
            if year % 400 == 0:  # If divisible by 400, it is a leap year
                return True
            else:
                return False  # Not a leap year if only divisible by 100
        else:
            return True  # Divisible by 4 but not 100, so it's a leap year
    else:
        return False  # Not divisible by 4, so not a leap year

# Example 
year = 2020
print(leap_year(year))  # Output will be True since 2020 is a leap year


#Problem 5
class Character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def check_tasks(self):
        # Task 1: Climb a mountain – needs rope, coat, and first aid kit, cannot have slow
        def climb_mountain():
            important_items = ['rope', 'coat', 'first aid kit']
            if all(item in self.weapons for item in important_items) and 'slow' not in self.weaknesses:
                print("Task 1: You can climb the mountain.")
            else:
                print("Task 1: You cannot climb the mountain. Missing items or you are slow.")
        
        # Task 2: Cook a meal – needs pan, groceries, cannot have small
        def cook_meal():
            important_items = ['pan', 'groceries']
            if all(item in self.weapons for item in important_items) and 'small' not in self.weaknesses:
                print("Task 2: You can cook a meal.")
            else:
                print("Task 2: You cannot cook a meal. Missing items or you have the 'small' debuff.")

        # Task 3: Write a book – needs pen, paper, idea, cannot have confusion
        def write_book():
            important_items = ['pen', 'paper', 'idea']
            if all(item in self.weapons for item in important_items) and 'confusion' not in self.weaknesses:
                print("Task 3: You can write a book.")
            else:
                print("Task 3: You cannot write a book. Missing items or you are confused.")

        # Run the checks for all tasks
        climb_mountain()
        cook_meal()
        write_book()


# Example usage
player1 = Character('Dragon Slayer', ['pan', 'paper', 'idea', 'rope', 'groceries'], ['slow'])

player1.check_tasks()
