from django.urls import path
from receitas import views

#receitas:receitas
app_name = 'receitas'

urlpatterns = [
    path('', views.home, name="home"),
    path('receitas/category/<int:category_id>/', views.category, name="category"),
    path('receitas/<int:id>/', views.receita, name="receitas"),
    
]