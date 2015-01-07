from django.conf.urls import patterns, include, url
from django.contrib import admin

from contact.views import MessageAddView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'biblio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^shelf/', include('shelf.urls', namespace='shelf') ),
    url(r'^contact/$', MessageAddView.as_view()),
    url(r'^accounts/', include('allauth.urls')),
    #~ url(r'^accounts/profile/$', MyProfileView.as_view()),
    
    url(r'^$', 'shelf.views.index_view', name='main-page'),
)


