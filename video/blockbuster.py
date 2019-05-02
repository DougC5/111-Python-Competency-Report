
import pickle
from menu import menu
from movie import Movie

inventory = []

data_file = "movie_inventory.dat"

def save_data():
    writer = open('data_file', "wb")
    pickle.dump(inventory, writer)
    writer.close()
    print('Data Saved!!')

def load_data():
    reader = open('data_file', 'rb')
    temp = pickle.load(reader)
    for movie in temp:
        inventory.append(movie) #Puts the vehicle back into the array

    print('Loaded from database: ' + str(len(inventory)))

def load_stock():
    user_id = int(len(inventory)) + 1
    m = Movie(user_id ,'Marry Popins', 2008, 13.5, 4)
    inventory.append(m)

    user_id = int(len(inventory)) + 1
    m = Movie(user_id ,'Good, Bad, and Ugly', 1976, 4.5, 6)
    inventory.append(m)

    user_id = int(len(inventory)) + 1
    m = Movie(user_id ,'Good Girls Dont Cry', 20014, 6, 6)
    inventory.append(m)

    save_data()


def register_new():
    print('Register new')
    try:
        user_title = input('\nTitle: ')
        user_year = int(input('Year: '))
        user_price = float(input('Price: '))
        user_stock = int(input('Stock: '))

        user_id = int(len(inventory)) + 1

        m = Movie(user_id ,user_title, user_year, user_price, user_stock)
        inventory.append(m)
        save_data() #saves the array to the file
        input('\nmovie added press enter to continue')

    except Exception as e:
        print('Some of the data is invalid. Please try again')
        print(e)
    return



def stock_check(full_list):
    for movie in inventory:
        if full_list == False and movie.stock == 0:
            continue #print(str(movie.movie_id) + ': ' + movie.title)
        else:
            print(str(movie.movie_id) + ': ' + movie.title)

    sel = int(input('\nPlease enter a movie number for details> '))
    if (sel > 0 and sel < int(len(inventory))):
        i = sel - 1
        m = inventory[i]
        print('\n')
        print('*' * 10)
        print('Movie Info:')
        print('ID: ' + str(m.movie_id) + '\nTitle: ' + m.title + '\nStock: ' + str(m.stock))
        print(('*' * 10) + '\n')
        return m
    
    else:
        return

def checkout():
    m = stock_check(False)
    if m.stock >= 1:
        m.stock = m.stock - 1
        input('You have successfully checked out: ' + m.title + '. ' + str(m.stock) + ' remaining' )
    
    else:
        input(m.title + ' is currently out of stock and cannot be checked out')
    save_data()

def return_movie():
    m = stock_check(True)
    m.stock = m.stock + 1
    input('You have successfully returned: ' + m.title + '. ' + str(m.stock) + ' in Stock' )
    save_data()
    

load_data() #load movies from file
selection = ''
while (selection != 'x' and selection != 'X'):
    selection = menu()

    if (selection == '1'):
        register_new()
    
    elif (selection == '2'):
        checkout()

    elif (selection == '3'):
        stock_check()

    elif (selection == '4'):
         return_movie()

    elif (selection == '5'):
         load_stock()
