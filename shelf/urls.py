from django.conf.urls import patterns, include, url

from shelf.views import AuthorListView, AuthorDetailView

urlpatterns = patterns('',
    url(r'^autorzy/$', AuthorListView.as_view(), name='author-list'),
    url(r'^autorzy/(?P<pk>\d+)/$', AuthorDetailView.as_view(), name='author-detail'),
)
