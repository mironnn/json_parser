from django.conf.urls import patterns, include, url
from django.contrib import admin
from json_app.views import index, open_file, load_chart, json_template

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my_json.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^index', index),
    url(r'^open_file', open_file),
    url(r'^load_chart', load_chart),
    url(r'^json_template', json_template),


)
