def perfectsquare(list):
    duplicate = []
    for i in list1:
        sqroot = i**.5
        if sqroot % 1 == 0:
            print(f"{i} from List is a Perfect square as: {sqroot} * {sqroot} = {i}")
            duplicate.append(i)
    if len(duplicate) == 0:
        print("No Perfect Squares In The List")
    else:
        print(f"The Perfect Squares in the List are: {duplicate}")
    return
    
    # Call Function to go through a list and discover any perfect squares
    # Outputs a list (duplicate) of the perfect squares found in any list
    # If No Perfect Squares, The Function returns that there are no squares in list
