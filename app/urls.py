from django.conf.urls import url, include
from . import views



app_name = 'app'



urlpatterns = [
	url(r'^$', views.index.as_view(), name='index'),
	
]