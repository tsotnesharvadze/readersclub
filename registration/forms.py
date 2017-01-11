from django import forms
from .models import Account
from django.utils.translation import ugettext_lazy as _
# import datetime

class UserUpForm(forms.ModelForm):
	first_name=forms.CharField(widget=forms.PasswordInput(attrs={
		'class':'form-control',
		'type':"text",
		'name':"first_name",
		'placeholder' : _('სახელი'),
		}),label=_('სახელი'), required=True)
	last_name=forms.CharField(max_length=50 ,widget=forms.TextInput(attrs={
		'class':'form-control',
		'type':"text",
		'name':"last_name",
		'placeholder' : _('გვარი'),
		}),label=_('გვარი'), required=True)
	email=forms.CharField(max_length=50 ,widget=forms.EmailInput(attrs={
		'class':'form-control',
		'type':"email",
		'name':"email",
		'placeholder' : _('ემაილი'),
		}),label=_('ემაილი'), required=True)
	phone=forms.CharField(widget=forms.NumberInput(attrs={
		'class':'form-control',
		'name' : 'phone',
		}), label=_("მობ.ტელეფონი"),required=True)
	password=forms.CharField(widget=forms.PasswordInput(attrs={
		'class':'form-control',
		'type':"password",
		'name':"password",
		'placeholder' : _('პაროლი'),
		}),label=_('პაროლი'), required=True)
	confpassword=forms.CharField(widget=forms.PasswordInput(attrs={
		'class':'form-control',
		'type':"password",
		'name':"confpassword",
		
		}),label=_('გაიმეორეთ პაროლი'), required=True)
	rules = forms.BooleanField(widget = forms.CheckboxInput(attrs={
		'type':'checkbox',
		'name' : 'rules',
		}),label= _('წესები'), required=True)
	personal_number = forms.IntegerField(widget=forms.NumberInput(attrs={
 		'class':'form-control',
 		'placeholder' : _('პირადი ნომერი'),
 		'name' : 'personal_number',
 		}), label=_("პირადი ნომერი"), required=True)
	sex = forms.ChoiceField(widget=forms.Select(attrs={
            'id' : 'sex',
            'class' : 'dropdown-select form-control'
        }), label=_('სქესი'), choices=Account.ASC)
	def clean_confpassword(self):
		# cleaned_data = super(UserUpForm, self).clean()
		password = self.cleaned_data['password']
		password1 = self.cleaned_data['confpassword']
		if password != password1:
			raise forms.ValidationError(_('პაროლის დადასტურება არ ემთხვევა პაროლს'))
		return password

	class Meta:
		model=Account
		fields=['first_name','last_name','email','phone','personal_number','password','confpassword','sex','rules']

class UserInForm(forms.Form):
	email=forms.CharField(max_length=50 ,widget=forms.EmailInput(attrs={
		'class':'form-control',
		'type':"email",
		'name':"email",
		'placeholder' : _('ემაილი'),
		}),label=_('ემაილი'))
	password=forms.CharField(widget=forms.PasswordInput(attrs={
		'class':'form-control',
		'type':"password",
		'name':"password",
		'placeholder' : _('პაროლი'),
		}),label=_('პაროლი'))

	class Meta:
		fields=['email','password']

class New_passwordForm(forms.Form):
	password=forms.CharField(widget=forms.PasswordInput(attrs={
	'class':'form-control',
	'style':"width: 30%;",
	}), label=_("პაროლი"))	
	confpassword=forms.CharField(widget=forms.PasswordInput(attrs={
	'class':'form-control',
	'style':"width: 30%;",
	}), label=_("დაადასტურე პაროლი"))
	class Meta:
		fields=["password","confpassword"]

# class UserForm(forms.ModelForm):
# 	first_name=forms.CharField(widget=forms.TextInput(attrs={
# 	'class':'form-control',
# 	'style':"width: 20%;",
# 	}), label=_("სახელი"))
# 	last_name=forms.CharField(widget=forms.TextInput(attrs={
# 	'class':'form-control',
# 	'style':"width: 20%;",
# 	}), label=_("გვარი"))
# 	username=forms.CharField(widget=forms.TextInput(attrs={
# 	'class':'form-control',
# 	'style':"width: 20%;",
# 	}), label=_("მეტსახელი"))
# 	email=forms.CharField(widget=forms.EmailInput(attrs={
# 	'class':'form-control',
# 	'style':"width: 30%;",
# 	}), label=_("ემაილი"))	
# 	born=forms.DateField(widget=forms.SelectDateWidget(attrs={
	
# 	},years=[x for x in range(datetime.datetime.now().year-80, datetime.datetime.now().year-15)]), label=_("დაბადების თარიღი"), required=False)	
# 	work_time=forms.DateField(widget=forms.SelectDateWidget(attrs={
# 	'class':'',
	
# 	}, years=[x for x in range(datetime.datetime.now().year-50, datetime.datetime.now().year+1)]), label=_("მუშაობის დაწყების დრო"), required=False)	
# 	location=forms.CharField(widget=forms.TextInput(attrs={
# 	'class':'form-control',
# 	'style':"width: 40%;",
# 	}), label=_("მდებარეობა"), required=False)	
# 	experience=forms.CharField(widget=forms.TextInput(attrs={
# 	'class':'form-control',
# 	'style':"width: 90%;",
# 	}), label=_("გამოცდილება"), required=False)	
# 	address=forms.CharField(widget=forms.TextInput(attrs={
# 	'class':'form-control',
# 	'style':"width: 90%;",
# 	}), label=_("მისამართი"), required=False)	
# 	avatar=forms.ImageField(widget=forms.FileInput(attrs={
# 	'class':'uplod-file input[type="file"]'
# 	}), label=_("სურათის განახლება"), required=False)	
# 	phone=forms.CharField(widget=forms.TextInput(attrs={
# 	'class':'form-control',
# 	'style':"width: 20%;",
# 	}), label=_("მობ.ტელეფონი"), required=False)	
# 	home_phone=forms.CharField(widget=forms.TextInput(attrs={
# 	'class':'form-control',
# 	'style':"width: 20%;",
# 	}), label=_("სახ.ტელეფონი"), required=False)	
# 	status=forms.CharField(widget=forms.Textarea(attrs={
# 	'class':'form-control',
# 	'style':"width: 90%;height:100px;",
# 	}), label=_("სტატუსი"), required=False)
# 	profession=forms.CharField(widget=forms.TextInput(attrs={
# 	'class':'form-control',
# 	'style':"width: 40%;",
# 	}), label=_("პროფესია"), required=False)			
# 	class Meta:
# 		model=Account
# 		fields=["first_name","last_name",'username',"email","phone","home_phone","born","location","address","profession","experience","work_time","avatar", "status"]


class EmailForm(forms.Form):
	email=forms.CharField(widget=forms.EmailInput(attrs={
	'class':"form-control input-lg",
	 'id':"myInput" ,
	 'placeholder':_('იმეილი ჩაწერეთ აქ') ,
	 'type':"text",
	  'name':"email",
	}), label="")
	
	class Meta:
		fields=['email']
			