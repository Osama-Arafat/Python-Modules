# name=input("Enter Your name : ")
# if name.isalpha():
#     print("your name is valid")
# else:
#     print("your name is not valid")


def validate_name(name):
    if name.isalpha():
        print("Your name is valid")
    else:
        print("Your name is not valid")


name=(input("Enter Your name : "))
validate_name(name)
