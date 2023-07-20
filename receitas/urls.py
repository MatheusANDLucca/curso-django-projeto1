from django.urls import path
from receitas import views

#receitas:receitas
app_name = 'receitas'

urlpatterns = [
    path('', views.home, name="home"),
    path('receitas/<int:id>/', views.receita, name="receitas"),
]