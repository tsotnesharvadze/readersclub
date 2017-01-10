from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import CategoryModel , BookModel



class CategoryModelForm(forms.ModelForm):
	class Meta:
		model = CategoryModel
		fields = ['title','slug']

class BookModelForm(forms.ModelForm):
	class Meta:
		model = BookModel
		fields = ['title','description','image','publisher','cover','page','retail_price','catalog_price']
		
