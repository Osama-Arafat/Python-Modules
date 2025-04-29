def Verify_email(email):

    if '@' in email and '.' in email:
        username, domain = email.split('@')
        if username and domain:
            x,y=domain.split('.')
            if x and y:
                return email
    

#  example@domain.com
while True:
    email = input("Enter your email: ")
    vaild_email=Verify_email(email)
    if vaild_email:
        break
    print("Please enter a valid email address.")


print(f"email is: {vaild_email}")