import sqlite3,os
from datetime import datetime

path = os.path.join('db','shopping_list.db')
connection = sqlite3.connect(path)
cursor = connection.cursor()

def create_tables():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS list (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            list_name TEXT NOT NULL,
            data TEXT NOT NULL
        )''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            value REAL NOT NULL,
            amount INTEGER NOT NULL,
            id_list INTEGER NOT NULL,
            FOREIGN KEY (id_list) REFERENCES list (id)
        )''')
    connection.commit()

def list_creator():
    data = datetime.today()
    list_name = input('List Name: ')
    cursor.execute('INSERT INTO list (list_name,data) VALUES (?,?)',(list_name,data,))
    connection.commit()

def add_item():
    print('Select the desired list, e.g., 1')
    db_return = list_lists()
    for lista in db_return:
        print(lista[0],lista[1])
    id_list = input('>: ')

    while True:
        product_name = input('Product Name: ')
        value = input('Product Value: ')
        amount = input('Product Amount: ')
        cursor.execute('INSERT into products (name,value,amount,id_list) VALUES (?,?,?,?)',(product_name,value,amount,id_list,)) 
        connection.commit()
        option = input('Adicionar novo item (y ou n) ? \n>: ')
        if option != 'y':
            break

def remove_item():
    lists = list_lists()
    print('Select the desired list, e.g., 1')
    for lista in lists:
        print(lista[0],lista[1])
    option = input('>: ')
    cursor.execute('SELECT * FROM products WHERE id_list = ?',(option,))
    products = cursor.fetchall()
    print('Select the product you want to delete, e.g., 12')
    for product in products:
        print(product[0:2])
    option = input('>: ')
    cursor.execute ('DELETE FROM products WHERE id = ?',(option,))
    connection.commit()
    
def edit_item():
    lists = list_lists()
    print('Select the desired list, e.g., 1')
    for lista in lists:
        print(lista[0],lista[1])
    option = input('>: ')
    cursor.execute('SELECT * FROM products WHERE id_list = ?',(option,))
    products = cursor.fetchall()
    for product in products:
        print(product[0:2])
    option1 = int(input('>: '))
    print('''What do you want to edit?
1 - Product Name
2 - Quantity
3 - Value''')
    option2 = int(input('>: '))
    match option2:
        case 1:
            new_value = input('Product Name: ')
            cursor.execute('UPDATE products SET name = ? where id = ?',(new_value,option1))
            connection.commit()
        case 2:
            new_value = input('Quantity: ')
            cursor.execute('UPDATE products SET amount = ? where id = ?',(new_value,option1))
            connection.commit()
        case 3:
            new_value = input('Value: ')
            cursor.execute('UPDATE products SET value = ? where id = ?',(new_value,option1))
            connection.commit()
        case _:
            print('Invalid Option')

def list_itens():
    lists = list_lists()
    print('Select the desired list, e.g., 1')
    for lista in lists:
        print(lista[0],lista[1])
    option = input('>: ')
    cursor.execute('SELECT * FROM products WHERE id_list = ?',(option,))
    products = cursor.fetchall()
    total = 0
    for product in products:
        print(product[1:4])
        total = total + product[3]*product[2]
    print(f'Total: R$ {'%.2f' %total}')

def list_lists():
    cursor.execute('SELECT * FROM list')
    return cursor.fetchall()
