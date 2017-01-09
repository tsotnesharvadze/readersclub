from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.utils.translation import ugettext_lazy as _
from re import search, findall

def get_index(section, CHOICES):
	for item in CHOICES:
		if section == item[1]:
			return item[0]
	return 0
	


def is_Admin(user):
	if user.is_authenticated():
		return user.is_admin
	return False



# slugify url

def convert(line):
	line = '-'.join(findall(r'\w+', line))
	return line

def is_ascii(s):
	return all(ord(c) < 128 for c in s)

def change(line):
	new_line = ''
	for letter in line:
		if is_ascii(letter):
			new_line += letter
		else:
			new_line += 'u' + str(ord(letter))
	return new_line

def slugify(line):
	line = convert(line)
	#line = change(line)
	return line

def slug_to_id(slug):
	num = search(r'\d+', slug).group() 
	return int(num)


def send_email(request,code,to_email,shinaarsi):
	url = "http://{}/helpdesk/problem/{}".format(request.META['HTTP_HOST'], str(code))
	from_email = settings.EMAIL_HOST_USER
	subject = _("ახალი პრობლემა!!!")
	message = _('პრობლემა დაამატა : {} -მ(მა), \n  შინაარსი : {}  \n ').format(request.user,shinaarsi)

	text_content = '{0}{1}'.format(message, url)
	html_content = '<p>{0}<a href="{1}">{1}</a><p>'.format(message, url)

	msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
	msg.attach_alternative(html_content, "text/html")
	msg.send()
