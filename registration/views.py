from django.shortcuts import render, redirect, get_object_or_404 ,reverse
from django.http import Http404, HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import get_language
from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from .forms import UserInForm,UserUpForm,New_passwordForm ,EmailForm
from .util import get_code,get_id
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from .models import Account
from django.views.generic import View
from django.http.response import Http404
from app.models import SlideModel , BookModel


def log_out(request):
	logout(request)
	return redirect("app:index")

def sing(request):
	# formin = UserInForm()
	# formup = UserUpForm()
	if request.method=="POST":
		if 'singin' in request.POST:
			formin = UserInForm(request.POST or None)
			if formin.is_valid():
				email=formin.cleaned_data['email']
				password=formin.cleaned_data['password']
				user=authenticate(email=email,password=password)
				if user is not None:
					if user.is_active:
						login(request,user)
						return redirect("app:index")
				# else:
				# 	formin.add_error(None,_('პაროლი ან ემაილი არასწორია'))
				# try:
				# 	user=Account.objects.get(email=email)
				# except:
				# 	return HttpResponse(_('იმეილი ან პაროლი არაზუსტია'))

				# if not user.is_active:
				# 	return HttpResponse(_("თქვენი ექაუნთი არ არის გააქტიურებული \n შეამოწმეთ იმეილი :  {} ").format("<a href='https://mail.google.com/'>{}</a>".format(user.email)))
			else:
				formup = UserUpForm()
				return render(request, "home.html",
					{'form1':formin,
					'form':formup,
					'books':BookModel.objects.all(),
					'slide_imgs' : SlideModel.objects.all(),
					})
		
		elif 'singup' in request.POST:
			formup = UserUpForm(request.POST or None)

			if formup.is_valid():
				user = formup.save(commit=False)
				first_name = formup.cleaned_data['first_name']
				last_name = formup.cleaned_data['last_name']
				password = formup.cleaned_data['password']
				user.set_password(password)
				
				

				user.is_active = False
				user.save()

				# -----------ადმინისტრატორის იმეილი

				email = 'tsotnesharvadze@gmail.com'
				url = "http://{}/admin/registration/account/{}/change/".format(request.META['HTTP_HOST'], str(user.id))

				from_email = settings.EMAIL_HOST_USER
				subject = _("ექაუნთის გააქტიურება")
				message = _('გადადით ლინკზე {0}-ს/ის ექაუნთის გასააქტიურებლად :').format(first_name+' '+last_name)

				text_content = '{0}{1}'.format(message, url)
				html_content = '<p>{0}<a href="{1}">{1}</a><p>'.format(message, url)

				msg = EmailMultiAlternatives(subject, text_content, from_email, [email])
				msg.attach_alternative(html_content, "text/html")
				msg.send()
				#-------------------------- მომხმარებლის იმეილი
				email = formup.cleaned_data['email']
				from_email = settings.EMAIL_HOST_USER
				subject = _("readersclub.ge")
				message = _('გილოცავთ!  {0} {1} წარმატებით გიარეთ რეგისტრაცია , ადმინისტრატორის თანხმობის შემდეგ გაგიაქტურდებათ ექაუნთი ').format(first_name,last_name)
				url = "http://{}".format(request.META['HTTP_HOST'])
				text_content = '{0}{1}'.format(message, url)
				html_content = '<p>{0}<a href="{1}">{1}</a><p>'.format(message, url)

				msg = EmailMultiAlternatives(subject, text_content, from_email, [email])
				msg.attach_alternative(html_content, "text/html")
				msg.send()

				return render(request, "registration/msg_verification.html", {})


			else:
				formin = UserInForm()
				return render(request, "home.html",
					{'form1':formin,
					'form':formup,
					'books':BookModel.objects.all(),
					'slide_imgs' : SlideModel.objects.all(),
					})

	return redirect('app:index')
	


def the_user_info(request,user_code):
	user_id = get_id(int(user_code))
	the_user =get_object_or_404(Account,id=user_id)
	if the_user.is_active:
		return HttpResponse(_("ექაუნთი უკვე გააქტიურებულია"))
	context = {
	'the_user':the_user,
	}
	return render(request,'registration/the_user_info.html',context)







def activate(request, user_id):
	try:
		user = Account.objects.get(id=user_id)

		if user is not None and user.is_active==False:
			user.is_active = True
			user.save()
			return redirect('app:index')
	except:
		raise Http404

	return HttpResponse(_("ექაუნთი უკვე გააქტიურებულია"))


class new_password(View):
	def post(self, request, *args, **kwargs):
		form = New_passwordForm(request.POST or None)
		if form.is_valid():
			password = form.cleaned_data['password']
			confpassword = form.cleaned_data['confpassword']
			if password == confpassword:
				try:
					user_id = get_id(int(kwargs['code']))
				
					user = get_object_or_404(Account , id =user_id)
				except Http404 :
					user = get_object_or_404(Account , id =kwargs['code'])
				
				if user.is_active:
					user.set_password(password)
					user.save()
					email = user.email
					user=authenticate(email=email,password=password)
					login(request,user)
					return redirect("app:index")
				else:
					return HttpResponse(_("თქვენი ექაუნთი არ არის გააქტიურებული"))
			else:
				return HttpResponse(_("პაროლი და დადასტურება ერთმანეთს არ ემთხვევა :("))
		else:
			return render(request, "registration/new_password.html",{'form':form})


	def get(self, request, *args, **kwargs):
		form = New_passwordForm()
		user = None
		try:
			print(kwargs['code'])
			user_id = get_id(int(kwargs['code']))
			user = get_object_or_404(Account , id =user_id)
		except Http404:
			user = get_object_or_404(Account , id =kwargs['code'])

		context = {
			"form": form,
			"user": user
		}
		return render(request, "registration/new_password.html", context)

class Profile(View):
	
	def post(self, request, *args, **kwargs):
		user = request.user #Account.objects.get(id=int(kwargs["user_id"]))
		if 'cancel' in request.POST:
			pass
		elif 'bio' in request.POST:
			form=UserForm(request.POST,request.FILES, instance=user)
			if form.is_valid():
				user = form.save()
				return redirect("registration:profile",user.id)
			else:
				return render(request, "registration/profile.html", self.get_context_data(
					form=form))
		elif 'pass' in request.POST:
			passform=New_passwordForm(request.POST)
			if passform.is_valid():
				password = passform.cleaned_data['password']
				confpassword = passform.cleaned_data['confpassword']
				if password == confpassword:

					user = request.user
					if user.is_active:
						user.set_password(password)
						user.save()
						user=authenticate(email=user.email,password=password)
						login(request,user)

			else:
				return HttpResponse(_("გთხოვთ სწორად შეავსოთ ველები .. "))
		return redirect("registration:profile",user.id)

	def get(self, request, *args, **kwargs) :
		user_prof = get_object_or_404(Account, id=int(kwargs["user_id"]))
		form = UserForm(instance=user_prof)
		context = {
			'user_prof':user_prof,
			"form" : form,
			'passform':New_passwordForm(),
			}
			
		return render(request, "registration/profile.html", context)


def email_send_for_new_password(request):
	form=EmailForm(request.POST or None)
	if request.method=="POST":
		if form.is_valid():
			to_email=form.cleaned_data['email']
			user=get_object_or_404(Account, email=to_email)
			code=get_code(user.id)
			url = "http://{}/registration/new_password/{}".format(request.META['HTTP_HOST'], str(code))

			from_email = settings.EMAIL_HOST_USER
			subject = _("პაროლის აღდგენა")
			message = _('გადადით ლინკზე თქვენი პაროლის არსადგენად :')

			text_content = '{0}{1}'.format(message, url)
			html_content = '<p>{0}<a href="{1}">{1}</a><p>'.format(message, url)

			msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
			msg.attach_alternative(html_content, "text/html")
			msg.send()

	return render(request,"registration/email_send_for_new_password.html", {'form':form})