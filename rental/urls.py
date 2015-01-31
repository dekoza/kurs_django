from django.conf.urls import patterns, include, url
from .views import BookRentView

urlpatterns = patterns('',
    url('^form/$', BookRentView.as_view(), name='rent-form'),
)
