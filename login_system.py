# user_list = [{"name": "omar", "pass": "123"}, {"name": "ahmed", "pass": "456"}]

# for attempt in range(5):
#     usr = input("Enter Your Username: ")

#     if not usr.isalpha():
#         print("Username must contain only alphabetic characters.")
#         continue

#     user_found = False  # Flag to check if username exists
#     for user in user_list:
#         if usr == user["name"]:
#             user_found = True
#             pswd = input("Enter Your Password: ")

#             if pswd == user["pass"] and pswd.isdigit():
#                 print("Welcome Back")
#                 exit()  # Exit the whole program if login is successful
#             else:
#                 print("Wrong password")
#                 break  # Exit the inner loop, but not the program

#     if not user_found:
#         print("Wrong username")

# else:
#     print("Your account is blocked. Please try again later.")


def login_system(user_list, max_attempts=5):
    for attempt in range(max_attempts):
        usr = input("Enter Your Username: ")

        if not usr.isalpha():
            print("Username must contain only alphabetic characters.")
            continue

        user_found = False
        for user in user_list:
            if usr == user["name"]:
                user_found = True
                pswd = input("Enter Your Password: ")

                if pswd == user["pass"] and pswd.isdigit():
                    print("Welcome Back")
                    return  # Successful login, exit the function
                else:
                    print("Wrong password")
                    break  # Exit inner loop, allow retry

        if not user_found:
            print("Wrong username")

    print("Your account is blocked. Please try again later.")


# # Example usage
# users = [{"name": "omar", "pass": "123"}, {"name": "ahmed", "pass": "456"}]
# login_system(users)












