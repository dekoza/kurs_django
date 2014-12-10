from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.http import HttpResponse

from .models import Author, Book


class MainPageView(TemplateView):
    template_name = 'index.html'

index_view = MainPageView.as_view()


class AuthorListView(ListView):
    model = Author


class AuthorDetailView(DetailView):
    model = Author


class BookListView(ListView):
    model = Book


class BookDetailView(DetailView):
    model = Book
