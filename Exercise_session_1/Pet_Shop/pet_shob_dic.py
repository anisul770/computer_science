
prices_dict = {'dog': 600.0, 'cat': 400.0, 'dog food': 10, 'cat food': 5}
is_pet_dict = {'dog': True, 'cat': True, 'dog food': False, 'cat food': False}


def discount(items):

    amount = 0
    items_contains_atleast_apet = False

    for item in items:
        if is_pet_dict[item]:
            items_contains_atleast_apet = True
        else:
            amount += prices_dict[item]

    if items_contains_atleast_apet:
        return 20*amount/100
    else:
        return 0


def main():

    item_list = list()

    item = input("Enter a item: ")
    while item != '':
        item_list.append(item)

        item = input('Enter an item: ')
    discounted_value = discount(item_list)
    print(f'The discounted value is: {discounted_value}')


main()
