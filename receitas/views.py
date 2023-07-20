from django.shortcuts import render
from utils.receitas.factory import make_recipe
from .models import Recipe

def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')
    return render(request, 'receitas/pages/home.html', context={
        'recipes': recipes,
    })

def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published=True
        ).order_by('-id')
    return render(request, 'receitas/pages/categoria.html', context={
        'recipes': recipes,
    })

def receita(request, id):
    return render(request, 'receitas/pages/receita-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page':True,
    })