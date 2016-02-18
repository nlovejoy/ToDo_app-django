from django.conf.urls import patterns, url
from social_todo import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^register$', views.register_user, name='register_user'),
        # url(r'^register2/$', views.register2, name='register2'),
        url(r'^logout$', views.user_logout, name='logout'),
        #url(r'^/user/login$', views.user_login, name='login'),
        url(r'^login$', views.login, name='login'),
        url(r'^create$', views.add_task, name='add_task'),
        url(r'^delete/([0-9]+)$', views.delete_task, name='delete_task'),
        url(r'^complete/([0-9]+)$', views.complete_task, name='complete_task'),
        )
