from django.conf.urls import url, include
from . import views



app_name = 'app'



urlpatterns = [
	url(r'^$', views.index.as_view(), name='index'),
	url(r'^book/(?P<pk>[0-9]+)/',views.detail.as_view() , name= 'detail'),

]