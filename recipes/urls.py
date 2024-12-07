from django.urls import path
from .import views


urlpatterns = [
    path('', views.RecipesListView.as_view(), name="recipes-home"),
    path('recipe/<int:pk>/', views.RecipesDetailView.as_view(), name="recipes-detail"),
    path('recipe/create/', views.RecipesCreateView.as_view(), name="recipes-create"),
    path('recipe/<int:pk>/update', views.RecipesUpdateView.as_view(), name="recipes-update"),
     path('recipe/<int:pk>/delete', views.RecipesDeleteView.as_view(), name="recipes-delete"),
    path('about/', views.about, name="recipes-about"),
    
]