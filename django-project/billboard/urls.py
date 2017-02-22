from django.conf.urls import url
from . import views
from django.conf.urls import include
from django.contrib.auth import views as authviews

urlpatterns = [
    url(r'^$', authviews.login, name = 'login'),
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^signup/success/$', views.success, name = "success"),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^login/$',views.index, name='index'),
    url(r'^logout/$', authviews.logout, {'next_page' : '/billboard'}, name = 'logout')
]
