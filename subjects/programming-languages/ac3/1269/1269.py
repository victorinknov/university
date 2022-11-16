list_of_products = []


def show_list():
    list_of_products.sort()
    text = ''
    for y in list_of_products:
        text += str(y) + ' '
    return text[:-1]

while True:
    user_input = input()
    curated_input = user_input.split()

    if user_input == '':
        None

    elif curated_input[0].isnumeric():
        for x in curated_input:
            list_of_products.append(int(x))

    elif curated_input[0] == 'adicionar':
        curated_input.pop(0)
        for x in curated_input:
            list_of_products.append(int(x))

    elif curated_input[0] == 'remover':
        curated_input.pop(0)
        remove_item = int(curated_input[0])
        if remove_item in list_of_products:
            list_of_products.remove(remove_item)
        else:
            print(f'código {remove_item} não encontrado')

    elif curated_input[0] == 'exibir':
        print(show_list())

    elif curated_input[0] == 'encerrar':
        print(show_list())
        break

    else:
        break
