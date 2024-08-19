from django.shortcuts import render
from django.http import HttpResponseBadRequest
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

}


def recipe_view(request, dish_name):
    servings = request.GET.get('servings')

    # Проверка на наличие servings в запросе
    if servings is None:
        servings = 1
    else:
        # Проверка на корректность параметра servings
        if not servings.isdigit() or int(servings) < 1:
            return HttpResponseBadRequest("Введите валидное целое значение 'servings'.")
        servings = int(servings)

    recipe = DATA.get(dish_name)

    if recipe:
        # Умножаем ингридиенты на значение srevings
        scaled_recipe = {ingredient: amount * servings for ingredient, amount in recipe.items()}
        context = {'recipe': scaled_recipe}
    else:
        context = {'recipe': None}

    return render(request, 'calculator/index.html', context)
