import requests


def recipe_search(ingredient, excluded):
    app_id = 'd09719e6'
    app_key = '3a4837a52d4a5061a7de09f9e033938a'
    result = requests.get('https://api.edamam.com/search?q={}&excluded={}&app_id={}&app_key={}'.format(ingredient,excluded, app_id, app_key))
    data = result.json()
    return data['hits']

def run():
    number_ingredients = int(input("How many ingredients do you want to use? (Max. 5 entries) "))
    global filter0
    global filter1
    global filter2
    global filtered

    ingredient = input('Enter your main 2 ingredients, separated by a comma: ')

    for i in range(number_ingredients - 2):
        globals()["filter" + str(i)] = input("Enter the next ingredient: ")

    excluded = input('Enter one ingredient to exclude (optional): ')
    calorie_check = input('Would you also like to search by calories? (yes or no) ')

    if calorie_check == 'yes':
        calorie_search = True
        no_of_calories = input('What is the maximum calories you want to consume (in numbers)? ')
    else:
        calorie_search = False

    #most_relevant_match_sort = sorted(recipe_search, key = lambda repo: )

    results = recipe_search(ingredient, excluded)

    with open('CFG_Team_4_file.txt', 'w', encoding='utf-8') as Team4:
        for result in results:
            recipe = result['recipe']
            list = (recipe['ingredientLines'])
            ingredientlist = '\n'.join(repr(item) for item in list)

            # if calorie_search == True and recipe['calories'] <= float(no_of_calories):
            #     print(recipe['label'])
            #     print(recipe['url'])
            #     print('Calories: ', recipe['calories'])
            #     print("Ingredients: ", '\n', (ingredientlist))
            #
            # elif calorie_search == False:
            if number_ingredients == 3:
                if ingredientlist.find(filter0) != -1:
                    print(recipe['label'])
                    print(recipe['url'])
                    print("Ingredients: ", '\n', (ingredientlist))
            elif number_ingredients == 4:
                if ingredientlist.find(filter0) or ingredientlist.find(filter1) != -1:
                    print(recipe['label'])
                    print(recipe['url'])
                    print("Ingredients: ", '\n', (ingredientlist))
            elif number_ingredients == 5:
                if ingredientlist.find(filter0) or ingredientlist.find(filter1) or ingredientlist.find(filter2)!= -1:
                    print(recipe['label'])
                    print(recipe['url'])
                    print("Ingredients: ", '\n', (ingredientlist))
            else:
                print(recipe['label'])
                print(recipe['url'])
                print("Ingredients: ", '\n', (ingredientlist))



            print(' ')

            Team4.writelines([recipe['label'], '\n', recipe['url'], '\n', "Ingredients: \n", (ingredientlist), '\n', ' \n'])



run()
