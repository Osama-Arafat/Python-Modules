
# We Can Import all the functions here and it will work
from find import find_i_positions

# text = input("Enter Text : ")
# i_positions=find_i_positions(text)

# print(i_positions)


print("===============================================================")

from login_system import login_system

# users = [{"name": "omar", "pass": "123"}, {"name": "ahmed", "pass": "456"}]
# login_system(users)


print("===============================================================")

from Mario_List import modify_list

# modify_list(10,"*")


print("===============================================================")

from multi_List import multiplication_List

x = int(input("Enter Your Num: "))
result = multiplication_List(x)
print(result)

print("===============================================================")

from multi_pattern import multiplication_pattern
num = input(" Enter Your Number : ")
multiplication_pattern(num)


print("===============================================================")

import process_numbers



print("===============================================================")
import star


print("===============================================================")

from valid import validate_name

name=(input("Enter Your name : "))
validate_name(name)

print("===============================================================")
from verify_email import Verify_email

while True:
    email = input("Enter your email: ")
    vaild_email=Verify_email(email)
    if vaild_email:
        break
    print("Please enter a valid email address.")


print(f"email is: {vaild_email}")


print("===============================================================")

from vowels import vowels_count
user_input = input("Enter your string: ")
vowel_count = vowels_count(user_input)
print("Number of vowels:", vowel_count)

