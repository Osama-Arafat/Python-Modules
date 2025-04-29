# x = input ("Enter Your String  ")
# vowel=["a","e","i","o","u"]
# c=0
# for i in range(len(x)):
#     if x[i] in vowel :
#         print(c)
#         c+=1


def vowels_count (text):
    vowels=["a","e","i","o","u"]
    c=0
    for char in text:
        if char in vowels:
            c=c+1
    return c
        


user_input = input("Enter your string: ")
vowel_count = vowels_count(user_input)
print("Number of vowels:", vowel_count)


