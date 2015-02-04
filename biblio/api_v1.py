# plik api_v1.py wewnątrz katalogu konfiguracyjnego projektu
# tutaj definiuję strukturę mojego API

from rest_framework import routers

from shelf.api import BookViewSet

router = routers.DefaultRouter()

router.register('books', BookViewSet)
