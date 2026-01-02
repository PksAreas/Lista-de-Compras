import functions

menu_pt_br = '''-----------Menu-----------
1 - Nova lista
2 - Adcionar Produto
3 - Remover Produto
4 - Editar Produto
5 - Exibir lista
0 - Sair
--------------------------'''
invalid_option_pt_br = 'opção invalida'

menu_en_us = '''-----------Menu-----------
1 - New List
2 - Add Product
3 - Remove Product
4 - Edit Product
5 - View List
0 - Exit
--------------------------'''
invalid_option_en_us = 'invalid option'

language = '''Select your preferred language.
1 - English
2 - Portuguese
>: '''

def main():
    functions.create_tables()
    while True:
        try:
            option = int(input(language))
            match option:
                case 1:
                    menu = menu_en_us
                    invalid = invalid_option_en_us
                    break
                case 2:
                    menu = menu_pt_br
                    invalid = invalid_option_pt_br
                    break
                case _:
                    print('Invalid Option')
        except ValueError:
            print('Invalid value entered.')

    while True:
        print(menu)
        try:
            option = int(input('>:'))

            match option:
                case 1:
                    functions.list_creator()
                case 2:
                    functions.add_item()
                case 3:
                    functions.remove_item()
                case 4:
                    functions.edit_item()
                case 5:
                    functions.list_itens()
                case 0:
                    break
                case _:
                    print(invalid)
        except ValueError:
            print('Invalid value entered.')

if __name__ =='__main__':
    main()