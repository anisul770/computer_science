def recipe(file):
    try:
        with open(file) as infile:
            ingredients = []
            line = infile.readline().strip()
            print(line)
            line = infile.readline().strip()
            while line != '':
                tmp = line.split(';')
                ingredients.append(tmp)
                print(f'{tmp[0]} - {int(tmp[1]):.1f}')
                line = infile.readline().strip()
        print()
        print(f'Number of ingredients {len(ingredients)}')
        print()
        return ingredients
    except IOError:
        print(f'{file} dose not exist')
        exit()


def cost_calories(ingredients, file):
    try:
        with open(file) as infile:
            line = infile.readline().strip()
            food = {}
            total_cost = 0
            total_calories = 0
            while line != "":
                tmp = line.split(';')
                food[tmp[0]] = tmp[1:len(tmp)]
                line = infile.readline().strip()
            for i in range(len(ingredients)):
                if ingredients[i][0] in food:
                    cost = float(food[ingredients[i][0]][0].strip())*(int(ingredients[i][1].strip())/1000)
                    calories = int(food[ingredients[i][0]][1].strip())*(int(ingredients[i][1].strip())/1000)
                    total_cost += cost
                    total_calories += calories
            print(f'Recipe cost: {total_cost:.3f}')
            print(f'Recipe calories: {total_calories}')
    except IOError:
        print(f'{file} does not exist')
        exit()


def main():
    ingredients = recipe('recipe.txt')
    cost_calories(ingredients, 'foods.txt')


if __name__ == '__main__':
    main()
