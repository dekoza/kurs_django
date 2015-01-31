from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Rental

# Create your views here.

class BookRentView(CreateView):
    model = Rental
    fields = ['who', 'what']
    success_url = '/'
