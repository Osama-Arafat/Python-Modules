# for i in range (5):
#     print (" " * (5-i) + "*" * i)


def star (n):
    for i in range(1,n+1):
        print(" " * (5-i) + "*" * i)

x=int(input("enter your num : "))
star(x)



