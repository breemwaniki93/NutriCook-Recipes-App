from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .import models


# Create your views here.
def home(request):
    recipes = models.Recipe.objects.all()
    context = {
         'recipes': recipes
    }
    return render(request, "home.html", context)
class RecipesListView(ListView):
     model = models.Recipe
     template_name = 'home.html'
     context_object_name = 'recipes'

class RecipesDetailView(DetailView):
     model = models.Recipe
     template_name = 'recipe_detail.html'

class RecipesCreateView(LoginRequiredMixin,CreateView):
     model = models.Recipe
     template_name = 'recipe_form.html'
     fields = ['title', 'description']

     def form_valid(self, form):
         form.instance.author = self.request.user
         return super().form_valid(form)

class RecipesUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
     model = models.Recipe
     template_name = 'recipe_form.html' 
     fields = ['title', 'description']

     def test_func(self):
          recipe = self.get_object()
          return self.request.user == recipe.author

     def form_valid(self, form):
         form.instance.author = self.request.user
         return super().form_valid(form)

class RecipesDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
     model = models.Recipe
     template_name = 'recipe_confirm_delete.html'
     success_url = reverse_lazy('recipes-home')

     def test_func(self):
          recipe = self.get_object()
          return self.request.user == recipe.author

def about(request):
     return render(request, "about.html", {'title':'about us page'})
    