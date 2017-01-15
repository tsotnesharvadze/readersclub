from django.shortcuts import render ,get_object_or_404, redirect#,render_to_response
# from django.conf import settings
from django.http import Http404, HttpResponse, JsonResponse
from django.utils.translation import ugettext_lazy as _
# from django.utils.translation import get_language
from django.views.generic import TemplateView ,DetailView , ListView
from .forms import BookModelForm 
from .models import SlideModel , BookModel ,CategoryModel , BasketModel ,OrderModel,BasketLine,ReadersclubModel
from registration.forms import UserUpForm ,UserInForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from registration.models import Account
from .helpers import slug_to_id #,get_index,send_email
from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt


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

	def post(self,request,*args,**kwargs):
		basket = request.user.basket
		if 'add' in request.POST:
			line = BasketLine.objects.create(
				user = request.user,
				book = get_object_or_404(BookModel,id = kwargs['pk']))
			basket.line.add(line)
		elif 'remove' in request.POST:
			line = basket.line.filter(book = get_object_or_404(BookModel,id = kwargs['pk']),user = request.user)[0]
			basket.line.remove(line)
			line.delete()

		return redirect('app:basket')
		
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
	object_list = None

	# def get_queryset(self):
	# 	basket = self.model.objects.get()
	# 	lst = basket.line.all()
	# 	return lst

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

	def get(self,request,*args,**kwargs):
		basket = request.user.basket
		return render(request , self.template_name , self.get_context_data( basket = basket ))
	def post(self,request,*args,**kwargs):
		if 'line_pk' in request.POST:
			pk = request.POST['line_pk']
			basket = request.user.basket
			line = get_object_or_404(BasketLine,id = pk)
			basket.line.remove(line)
			line.delete()
			basket.save()

			return JsonResponse({"id":pk,'total_price':basket.get_total_price(),'length':len(basket.line.all())})
		
		elif 'line_pk_price' in request.POST:
			pk = request.POST['line_pk_price']
			basket = request.user.basket
			line = get_object_or_404(BasketLine,id = pk)
			quantity = request.POST['quantity']
			line.quantity = int(quantity)
			line.save()
			price = line.get_price()
			retail_price = line.book.get_wholesale_price()
			book = line.book.title


			return JsonResponse({"id":pk,
								'total_price':basket.get_total_price(),
								'price' : price,
								'quantity':quantity,
								'retail_price' : retail_price,
								'book' : book,
								})


class Order(ListView):
	template_name = 'order_placement.html'
	model = BasketModel
	object_list = None


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

	def get(self,request,*args,**kwargs):
		basket = request.user.basket
		return render(request , self.template_name , self.get_context_data( basket = basket ))

	def post(self,request,*args,**kwargs):
		user = request.user
		basket = user.basket
		order = OrderModel.objects.create(
			user  = user,
			address = request.POST['address'],
			total = basket.get_total_price(),
			)
		
		for line in basket.line.all():
			order.line.add(line)
			basket.line.remove(line)
		order.save()
		basket.save()


		return render(request ,template_name =  'success.html')



class About(DetailView):
	template_name = 'about.html'
	model = ReadersclubModel
		