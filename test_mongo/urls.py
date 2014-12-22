from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test_mongo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blog.views.index'),
    url(r'^update/', 'blog.views.update'),
    url(r'^delete/', 'blog.views.delete'),
#    url(r'^blog/index/$', index),
)
