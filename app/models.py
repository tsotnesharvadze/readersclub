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
	slug = models.SlugField(max_length=250, unique = True, null = True , blank=True)

	def __str__(self):
		return self.title
	class Meta:
		verbose_name = _('კატეგორია')
		verbose_name_plural = _('კატეგორიები')

class BookModel(AbsTime):
	title = models.CharField(_('სათაური'), max_length=200,  default='')
	description = RichTextField(_('აღწერა'), default='')
	image = models.FileField(verbose_name=_("სურათი"),upload_to='books_img/', null=True)
	publisher=models.CharField(verbose_name=_("გამომცემლობა"),max_length=200,null=True)
	cover=models.CharField(verbose_name=_("ყდა"),max_length=200,null=True)
	page = models.IntegerField(_('გვერდი'), default=1)
	retail_price = models.DecimalField(_('საცალო ფასი'),null=True,max_digits=6, decimal_places=2)
	catalog_price = models.DecimalField(_('კატალოგის ფასი'),null=True,max_digits=6, decimal_places=2)
	category = models.ForeignKey(CategoryModel, null=True, verbose_name=_('კატეგორია'))

	# price = models.DecimalField(max_digits=6, decimal_places=2)
	# retail_price = models.IntegerField(_('საცალო ფასი'), default=1)
	# catalog_price = models.IntegerField(_('კატალოგის ფასი'), default=1)

	def __str__(self):
		return self.title

	def get_wholesale_price(self):
		return round(((self.retail_price * 85)/100),2)
	class Meta:
		verbose_name = _('წიგნი')
		verbose_name_plural = _('წიგნები')


class SlideModel(AbsTime):
	img = models.ImageField(verbose_name=_("სურათი"),upload_to='slideshow_img/')
	title = models.CharField(_('სათაური'), max_length=200, null= True,  default='')

	def __str__(self):
		return self.img.url
	class Meta:
		verbose_name = _('სლაიდის სურათი')
		verbose_name_plural = _('სლაიდის სურათები')





@receiver(post_save, sender=CategoryModel)
def p_save(sender, **kwargs):

	object = kwargs.get("instance")	

	if kwargs['created']:
		object.slug = '%d-%s' % (object.id, slugify(object.title))
		object.save()

	elif len(object.slug)==1: 
		object.slug = '%d-%s' % (object.id, slugify(object.title))
		object.save()
