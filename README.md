# Recipe_App
#A recipe search app that utilizes Edaman API and TKinter framework
#Main_file_is_the_project_source_code
#Other_files_are_Extended_idea_for_Recipe_Search_App_project

#Find_Main_file_source_code_below

import requests

def recipe_search(ingredient):
  app_id = 'd09719e6'
  app_key = '3a4837a52d4a5061a7de09f9e033938a'
  result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id,app_key) )
  data = result.json() 
  
  return data['hits']

def run():
  ingredient = input('Enter an ingredient: ')
  
  results = recipe_search(ingredient)
  
  with open('CFG_Team_4_file.txt', 'w', encoding='utf-8') as Team4:
    for result in results:
      recipe = result['recipe']
      list = (recipe['ingredientLines'])
      ingredientlist = '\n'.join(repr(item) for item in list)

      print(recipe['label'])
      print(recipe['url'])
      print("Ingredients: ", '\n', (ingredientlist))
      print (' ')

      Team4.writelines([recipe['label'], '\n', recipe['url'], '\n', "Ingredients: \n", (ingredientlist), '\n', ' \n'])

run()
