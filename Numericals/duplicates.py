def remove_duplicate():
    input_string = int(input("Enter a list numbers or elements separated by space: "))
    duplicate = input_string.split()
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

print (remove_duplicate())
