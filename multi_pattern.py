# x=input("Enter Your Num ")
# x = int(x)
# for i in range (1,x+1):
#     for j in range (1,i+1):
#         print (f"{i}x{j}={i*j}")


def multiplication_pattern(n):
    n=int(n)
    for i in range(n+1):
        for j in range (i+1):
            print (f"{i}x{j}={i*j}")


num = input(" Enter Your Number : ")
multiplication_pattern(num)