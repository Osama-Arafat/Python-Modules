# x=input("Enter Your Num ")
# x = int(x)
# a=[]
# for i in range(1,x+1):
#     b=[]
#     for e in range(1,i+1):
#         b.append(i*e)
#     a.append(b)   
# print(a)    


def multiplication_List(num):
    a = []
    for i in range(1, num + 1):
        b = []
        for e in range(1, i + 1):
            b.append(i * e)
        a.append(b)
    return a

x = int(input("Enter Your Num: "))
result = multiplication_List(x)
print(result)