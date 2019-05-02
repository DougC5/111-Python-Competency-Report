def menu():
    print("\n" + ("-" * 30))
    print(" *** Welcome to Blockbuster ***")
    print("-" * 30)
    print("1 - Register a new movie in the system")
    print("2 - Checkout a movie")
    print('3 - See a list of movies in stock')
    print('4 - Return a movie')
    print('5 - Load the base stock in the system')
    print("X - to exit the system \n")
    opt = input("Please choose an option> ")
    return opt