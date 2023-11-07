#
def discount(prices, is_pet):

    amount = 0
    if True in is_pet:

        for i in range(len(prices)):
            if not is_pet[i]:
                amount = amount + prices[i]
    return 20*amount/100

def main():

   prices_list = list()
   is_pet_list = list()
   price = float(input('Enter a price: '))
   while price != -1:
       prices_list.append(price)

       input_from_user = input('Is This is a pet? (y/n)').strip().lower()
       is_pet = input_from_user.startswith('y')
       is_pet_list.append(is_pet)
       price = float(input('Enter a price: '))

   discounted_value = discount(prices_list, is_pet_list)
   print(f'The discounted value is {discounted_value}')
main()
