from django.conf.urls import url, include
from . import views



app_name = 'app'



urlpatterns = [
	url(r'^$', views.index.as_view(), name='index'),
	url(r'^book/(?P<pk>[0-9]+)/',views.detail.as_view() , name= 'detail'),
	url(r'^category/$',views.Category.as_view() , name = 'category'),
	url(r'^category/(?P<slug>[-\w\W]+)/$',views.Category.as_view() , name = 'slug_category'),
	url(r'^basket/$',views.Basket.as_view() , name = 'basket'),
	url(r'^basket/order/' , views.Order.as_view() , name = 'order'),
	url(r'^about/(?P<pk>[0-9]+)/$' ,views.About.as_view(), name = 'about'),
	# url(r'^success/$ , )


]