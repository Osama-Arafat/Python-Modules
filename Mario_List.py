# x = [" "," "," "," "," "]
# for i in range (len(x)):
#     del x [0]
#     x.insert(len(x),"*")
#     print(x)
#     print(''.join(x))


def modify_list(space_count=5, char='*'):
    x = [' '] * space_count  # Initialize list with the specified number of spaces
    
    for i in range(space_count):
        del x[0]
        x.append(char)  # Append the character to the end of the list
        print(x)
        print(''.join(x))


# modify_list(10,"#")