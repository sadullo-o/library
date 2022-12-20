from django.shortcuts import render
from django.views.generic import ListView
from .models import Book, Comments
# Create your views here.


class BookListView(ListView):
    template_name = 'book_list.html'
    model = Book
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['books'] = Book.objects.all()
        context['comments'] = Comments.objects.all()
        return context
    # a = Comments.objects.all()
    # print(a[2].post_id)
