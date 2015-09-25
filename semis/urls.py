from django.conf.urls import patterns, url
from semis import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^login/$', views.login, name='login'),

                       #url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
                       #url(r"^(?P<question_id>\d+)/result/$", views.results, name='results'),
                       #url(r'^(?P<question_id>\d+)/votre/$', views.vote, name='vote'),

                       )