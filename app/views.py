from django.shortcuts import render ,get_object_or_404#, redirect,render_to_response
# from django.conf import settings
from django.http import Http404, HttpResponse, JsonResponse
from django.utils.translation import ugettext_lazy as _
# from django.utils.translation import get_language
from django.views.generic import TemplateView ,DetailView
from .forms import BookModelForm 
from .models import SlideModel , BookModel
from registration.forms import UserUpForm ,UserInForm
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
		context['form1'] = UserInForm()
		return context


class detail(DetailView):
	template_name = 'item-details.html'
	model = BookModel
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['related_books'] = BookModel.objects.filter(category = self.object.category).exclude(title = self.object.title)[:4]
		return context
		
