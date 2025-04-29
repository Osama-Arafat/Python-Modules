
# x=input (" Enter Your Name ")


# for y in range(len(x)):
#      if x[y]=="i":
#        print (y)



def find_i_positions(text):
    positions = []
    for index in range(len(text)):
        if text[index] == "i":
            positions.append(index)
    return positions


# text = input("Enter Text : ")
# i_positions=find_i_positions(text)

# print(i_positions)






