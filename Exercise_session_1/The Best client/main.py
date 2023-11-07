#

def main():
    sales = []
    customers = []
    day_end = False
    while not day_end:
        sale = int(input("Total bill: "))
        if sale != 0:
            sales.append(sale)
            Name = input("Customer Name: ").strip().upper()
            if Name in customers:
                index = customers.index(Name)
                sales[index] = sales[index] + sale
                sales.pop()
            else:
                customers.append(Name)
            finish = input("End of the day? (y/n)").strip().lower()
            if finish.startswith('y'):
                day_end = True
        else:
            continue
    print(sales, customers)
    best = name_of_best_customer(sales, customers)
    print(f'Top customer is {best[1]} purchased {best[0]} euro')


def name_of_best_customer(sales, customers):
    max = sales[0]
    max_index = 0
    for i in range(len(sales)):
        if max < sales[i]:
            max = sales[i]
            max_index = i
    Name = customers[max_index]

    return (max, Name)


main()
