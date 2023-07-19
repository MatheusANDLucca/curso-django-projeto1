from django.shortcuts import render

def home(request):
    return render(request, 'receitas/pages/home.html', context={
        'name': 'Matheus Lucca',
    })

def receita(request, id):
    return render(request, 'receitas/pages/receita-view.html', context={
        'name': 'Matheus Lucca',
    })