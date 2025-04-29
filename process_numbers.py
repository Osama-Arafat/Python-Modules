# List=[]
# print("Enter Your 5 Numbers")
# for i in range(5):
#     List.append(input(": "))

# print(List)
# x=sorted(List)
# y=sorted(List,reverse=True)
# print(x)
# print(y)



# def process_numbers():
#     numbers = []
#     print("Enter Your 5 Numbers")
#     for i in range(5):
#         numbers.append(input(": "))

#     print("Original List:", numbers)
#     ascending = sorted(numbers)
#     descending = sorted(numbers, reverse=True)
#     print("Sorted Ascending:", ascending)
#     print("Sorted Descending:", descending)



def process_numbers():
    try:
        count = int(input("How many numbers do you want to enter? "))
        numbers = []

        print(f"Enter {count} numbers:")
        for i in range(count):
            while True:
                try:
                    num = int(input(f"Number {i + 1}: "))
                    numbers.append(num)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

        print("Original List:", numbers)
        print("Sorted Ascending:", sorted(numbers))
        print("Sorted Descending:", sorted(numbers, reverse=True))

    except ValueError:
        print("Invalid input for count. Please enter an integer.")





process_numbers()










