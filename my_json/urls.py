from django.conf.urls import patterns, include, url
from django.contrib import admin
from json_app.views import index, open_file

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my_json.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^open_file', open_file),
)
