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
    template_name = "book_list.html"


class MultipleModelView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
         context = super(MultipleModelView, self).get_context_data(**kwargs)
         context['book'] = Book.objects.all()
         context['category'] = Category.objects.all()
         return context

def sort_by (request):
    book = Book.objects.filter(category__name="Python")
    return render(request, 'core/python_books.html', {
        "book": book,
    })

class CategoryView(generic.ListView):
    model = Book
    template_name ='core/python_books.html'
    
    def get_queryset(self):
        id = self.kwargs['pk']
        category=get_object_or_404(Category, pk = id)
        return Book.objects.filter(category=category)
        
    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['name'] = get_object_or_404(Category, pk = self.kwargs['pk'])
        return context