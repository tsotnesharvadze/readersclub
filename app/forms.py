from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import CategoryModel , BookModel



# class CategoryModelForm(forms.ModelForm):
# 	class Meta:
# 		model = CategoryModel
# 		fields = ['title','slug']

# class BookModelForm(forms.ModelForm):
# 	class Meta:
# 		model = BookModel
# 		fields = ['title','description','image','publisher','cover','page','retail_price','catalog_price']
		
class ContactForm(forms.Form):
	full_name_contact=forms.CharField(widget=forms.TextInput(attrs={
		'class':'form-control',
		'type':"text",
		'name':"full_name_contact",
		'placeholder' : _('სრული სახელი'),
		'data-validation-required-message':_('ჩაწერეთ თქვენი სრული სახელი'),
		}),label=_('სრული სახელი'), required=True)
	email_contact=forms.CharField(max_length=50 ,widget=forms.EmailInput(attrs={
		'class':'form-control',
		'type':"email",
		'name':"email_contact",
		'placeholder' : _('ემაილი'),
		'data-validation-required-message':_('ჩაწერეთ თქვენი იმეილი'),
		}),label=_('ემაილი'), required=True)
	phone_contact=forms.CharField(widget=forms.NumberInput(attrs={
		'class':'form-control',
		'name' : 'phone_contact',
		'data-validation-required-message':_('ჩაწერეთ თქვენი ტელეფონის ნომერი'),
		}), label=_("ტელეფონი"),required=True)
	message_contact=forms.CharField(widget=forms.Textarea(attrs={
		'class':'form-control',
		'type':"text",
		'name':"message_contact",
		'placeholder' : _('წერილი'),
		'data-validation-required-message':_('დაწერეთ წერილი'),
		}),label=_('წერილი'), required=True)
	class Meta:
 		fields = ['full_name','phone','email','message']