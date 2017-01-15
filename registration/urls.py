from django.conf.urls import url
from .views import *

app_name="registration"

from django.contrib.auth.decorators import login_required as x

urlpatterns=[
 url(r'^sing/$',sing,name="sing"),
 url(r'^log_out/$',log_out,name="log_out"),
 url(r'^activate/(?P<user_id>[0-9]+)/$',activate,name="activate"),
 url(r'^the_user_info/(?P<user_code>[0-9]+)/$',the_user_info,name="the_user_info"),
 url(r'^new_password/(?P<code>[-\d]+)/$',new_password.as_view(),name="new_password"),
 url(r'^profile/(?P<pk>[0-9]+)/$',Profile.as_view(),name="profile"),
 url(r'^email_send_for_new_password/$',email_send_for_new_password,name="email_send_for_new_password"),
# url(r'^(?P<posti_id>[0-9]+)/srulad/$',srulad,name="srulad"),
# url(r'^create_account/$',create_account,name="create_account"),





]