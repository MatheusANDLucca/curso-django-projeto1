from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'receitas/pages/home.html', context={
        'name': 'Matheus Lucca',
    })