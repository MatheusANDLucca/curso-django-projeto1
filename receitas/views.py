from django.shortcuts import render
from utils.receitas.factory import make_recipe

def home(request):
    return render(request, 'receitas/pages/home.html', context={

        'recipes': [make_recipe() for _ in range(10)],
    })

def receita(request, id):
    return render(request, 'receitas/pages/receita-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page':True,
    })