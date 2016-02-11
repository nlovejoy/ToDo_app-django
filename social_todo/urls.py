from django.conf.urls import patterns, url
from social_todo import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^register/$', views.register, name='register'),
        url(r'^register2/$', views.register2, name='register2'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^add_task/$', views.add_task, name='add_task'),
        )
