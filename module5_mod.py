class ReadUserInput:
    def __init(self):
        pass

    @staticmethod
    def read_input():
        # The program asks the user for input N (positive integer) and reads it
        num = int(input("Enter a positive integer you would like me to read: "))
        print("You entered: ", num)

        # The program asks the user to provide N numbers (one by one) and reads all of them (again, one by one)
        usr_inp = int(input("How many numbers you would like me to read? "))
        stored_nums = []
        for _ in range(usr_inp):
            num = int(input("Enter number: "))
            stored_nums.append(num)
            print("You entered: ", num)

        # The program asks the user for input X (integer) and outputs: "-1" if there were no such X among N read numbers, or the index (from 1 to N) of this X if the user inputed it before.
        num = int(input("Enter a number you want me to check if it was read before: "))
        if num in stored_nums:
            print("Index of the number is: ", stored_nums.index(num) + 1)
        else:
            print("-1")


# Creating an object of the class
obj = ReadUserInput()

# Calling class method using obj of the class
obj.read_input()
