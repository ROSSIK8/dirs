from django.shortcuts import render, HttpResponse
from decimal import Decimal


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def calculate_recipe_view(request, recipe_title):
    if recipe_title not in DATA:
        return HttpResponse('Такого рецепта не знаю :(')

    data = DATA[recipe_title]
    context = {
        'dish_name': recipe_title,
        'recipe': data
    }
    servings = request.GET.get('servings', None)
    if servings:
        dict_data = {}
        for key, val in data.items():
            dict_data[key] = Decimal(str(val)) * int(servings)
        context['recipe'] = dict_data


    return render(request, 'calculator/index.html', context)

