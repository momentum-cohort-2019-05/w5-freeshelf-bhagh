from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.views.generic import TemplateView

from core.models import Book, Author, Category

class BookListView(generic.ListView):
    model = Book

    def get_category():
        categories = Category.objects.all()
        return categories

class CategoryListView(generic.ListView):
    model = Category


from django.views.generic import TemplateView

class MultipleModelView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
         context = super(MultipleModelView, self).get_context_data(**kwargs)
         context['book'] = Book.objects.all()
         context['category'] = Category.objects.all()
         return context