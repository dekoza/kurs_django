from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from shelf.views import (AuthorListView, AuthorDetailView, BookListView,
    BookDetailView)
from rental.views import BookRentView

urlpatterns = patterns('',
    url(r'^autorzy/$', AuthorListView.as_view(), name='author-list'),
    url(r'^autorzy/(?P<pk>\d+)/$', AuthorDetailView.as_view(), name='author-detail'),
    url(r'^ksiazki/$', BookListView.as_view(), name='book-list'),
    url(r'^ksiazki/(?P<pk>\d+)/$', BookDetailView.as_view(), name='book-detail'),
    url(r'^ksiazki/(?P<pk>\d+)/rent/$', BookRentView.as_view(), name='book-rent'),
    
)
