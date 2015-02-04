# plik api.py wewnątrz aplikacji
# definicje widoków (ViewSet, View itd.)

from rest_framework.viewsets import ModelViewSet

from .models import Book

class BookViewSet(ModelViewSet):
    model = Book
