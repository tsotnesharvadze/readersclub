from django.shortcuts import render #, redirect, get_object_or_404 ,render_to_response
# from django.conf import settings
from django.http import Http404, HttpResponse, JsonResponse
from django.utils.translation import ugettext_lazy as _
# from django.utils.translation import get_language
from django.views.generic import TemplateView
from .forms import BookModelForm 
from .models import SlideModel , BookModel
from registration.forms import UserUpForm
from registration.views import sing
# from registration.models import Account
# from .helpers import get_index, slug_to_id,send_email

# class BookView(DetailsView):
# 	model = BookModel
# 	template_name = ''

class index(TemplateView):
	template_name = 'home.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['slide_imgs'] = SlideModel.objects.all()
		context['books'] = BookModel.objects.all()
		context['form'] = UserUpForm()
		return context