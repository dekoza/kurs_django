from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Author, Book



class MainPageView(TemplateView):
    template_name = 'index.html'

index_view = MainPageView.as_view()


class AuthorListView(ListView):
    model = Author

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        super(AuthorListView, self).dispatch(*args, **kwargs)


class AuthorDetailView(DetailView):
    model = Author


class BookListView(ListView):
    model = Book
        

class BookDetailView(DetailView):
    model = Book



