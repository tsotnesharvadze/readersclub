from django.db import models
from .helpers import slugify
from django.dispatch import receiver
from django.db.models.signals import post_save
from ckeditor.fields import RichTextField
from django.utils.translation import ugettext_lazy as _


class AbsTime(models.Model):
	created = models.DateTimeField(_('შეიქმნა'), auto_now_add=True, null=True)
	updated = models.DateTimeField(_('განახლდა'), auto_now=True, null=True)

	class Meta:
		abstract = True


class CategoryModel(AbsTime):
	title = models.CharField(_('სათაური'), max_length=200,  default='')
	slug = models.SlugField(max_length=250, unique = True, null = True)

class BookModel(AbsTime):
	title = models.CharField(_('სათაური'), max_length=200,  default='')
	description = RichTextField(_('აღწერა'), default='')
	image=models.FileField(verbose_name=_("სურათი"),upload_to='imgs', null=True)
	publisher=models.CharField(verbose_name=_("გამომცემლობა"),max_length=200,null=True)
	cover=models.CharField(verbose_name=_("ყდა"),max_length=200,null=True)
	page = models.IntegerField(_('გვერდი'), default=1)
	retail_price = models.IntegerField(_('საცალო ფასი'), default=1)
	catalog_price = models.IntegerField(_('კატალოგის ფასი'), default=1)
	
	def __str__(self):
		return self.title

	def get_wholesale_price(self):
		return (self.retail_price * 85)/100



@receiver(post_save, sender=CategoryModel)
def p_save(sender, **kwargs):

	object = kwargs.get("instance")	

	if kwargs['created']:
		object.slug = '%d-%s' % (object.id, slugify(object.title))
		object.save()

	elif len(object.slug)==1: 
		object.slug = '%d-%s' % (object.id, slugify(object.title))
		object.save()
