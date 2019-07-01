from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.views.generic.edit import CreateView
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib import messages
from datetime import datetime
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm



from core.models import Book, Author, Category, Favorite






class MultipleModelView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
         context = super(MultipleModelView, self).get_context_data(**kwargs)
         context['book'] = Book.objects.all()
         context['category'] = Category.objects.all()
         return context



class FavoriteView(TemplateView):
    template_name = 'core/favorites.html'

    def get_context_data(self, **kwargs):
         context = super(FavoriteView, self).get_context_data(**kwargs)
         context['book'] = Book.objects.all()
         context['category'] = Category.objects.all()
         return context
  

class CategoryView(generic.ListView):
    model = Book
    template_name ='core/category.html'
    
    def get_queryset(self):
        id = self.kwargs['pk']
        category=get_object_or_404(Category, pk = id)
        return Book.objects.filter(category=category)
        
    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['name'] = get_object_or_404(Category, pk = self.kwargs['pk'])
        context['category'] = Category.objects.all()

        return context

@login_required
def add_to_favorite(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    user = request.user
    next = request.POST.get('next', '/')
   
    favorite, created = user.favorite_set.get_or_create(book=book)
    user.favorited_at = datetime.now()

    if created: 
        messages.success(request, f"You've added {book.title} to your favorites.")
        book.times_favorited += 1
        book.save(update_fields=['times_favorited'])
    else: 
        messages.info(request, f"You've removed {book.title} from your favorites.")
        book.times_favorited -= 1
        book.save(update_fields=['times_favorited'])
        favorite.delete()

    return HttpResponseRedirect(next)

def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
    else:
        form = UserCreationForm()

        args = {'form': form}
        return render(request, 'registration/reg_form.html', args)

