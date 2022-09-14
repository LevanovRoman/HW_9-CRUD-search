from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import *
from .forms import *

menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'Добавить', 'url_name': 'add_post'},
]
class HomePage(ListView):
    model = RestaurantModel
    template_name = 'mainapp/home.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная'
        return context

class AddPost(CreateView):
    form_class = RestaurantForm
    template_name = 'mainapp/add_post.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Добавление поста'
        return context

class ShowPost(DetailView):
    model = RestaurantModel
    template_name = 'mainapp/show_post.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Вывод поста'
        return context

class PutPost(UpdateView):
    model = RestaurantModel
    template_name = 'mainapp/put_post.html'
    fields = '__all__'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Изменение поста'
        return context

class DelPost(DeleteView):
    model = RestaurantModel
    template_name = 'mainapp/del_post.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Удаление поста'
        return context

class SearchResult(ListView):
    model = RestaurantModel
    template_name = 'mainapp/search_result.html'
    context_object_name = 'post'

    def get_queryset(self):
        query = self.request.GET.get('q').capitalize()
        object_list = RestaurantModel.objects.filter(specialization__icontains=query)
        return object_list
