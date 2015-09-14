from django.conf.urls import patterns, url
from polls import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
                       url(r"^(?P<question_id>\d+)/result/$", views.results, name='results'),
                       url(r'^(?P<question_id>\d+)/votre/$', views.vote, name='vote'),
                       )
