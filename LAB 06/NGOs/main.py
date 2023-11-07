def subsidy(income, child):
    if 30000 <= income < 40000 and child >= 3:
        print('The subsidy is $1000 for each child')
    elif 20000 <= income < 30000 and child >= 2:
        print('The subsidy is $1500 for each child')
    elif income < 20000:
        print('The subsidy is $2000 for each child')
    else:
        print('You are rich')


def main():
    income = int(input('Enter your income: ').strip())
    while income != -1:
        child = int(input('Number of Child: ').strip())
        subsidy(income, child)
        income = int(input('Enter your income: ').strip())


if __name__ == '__main__':
    main()
