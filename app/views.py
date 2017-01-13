from django.shortcuts import render ,get_object_or_404#, redirect,render_to_response
# from django.conf import settings
from django.http import Http404, HttpResponse, JsonResponse
from django.utils.translation import ugettext_lazy as _
# from django.utils.translation import get_language
from django.views.generic import TemplateView ,DetailView , ListView
from .forms import BookModelForm 
from .models import SlideModel , BookModel ,CategoryModel , BasketModel
from registration.forms import UserUpForm ,UserInForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from registration.models import Account
from .helpers import slug_to_id #,get_index,send_email

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
		
class Category(ListView):
	template_name = 'category.html'
	model = BookModel
	paginate_by = 2

	def get_queryset(self):
		slug = self.kwargs.get('slug', None)
		if slug != None :
			category_id = slug_to_id(slug)
			lst = self.model.objects.order_by(self.get_ordering()).filter(category = get_object_or_404(CategoryModel,id =category_id))
		else :
			lst = self.model.objects.order_by(self.get_ordering())	
		return lst

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['categories'] = CategoryModel.objects.all()
		return context
	def get_ordering(self):
		self.ordering = '-created'
		return self.ordering


class Basket(ListView):
	template_name = 'shoppingbag.html'
	model = BasketModel

	
	