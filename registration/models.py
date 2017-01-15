from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models

from app.models import BasketModel

class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('მომხმარებელს უნდა ქონდეს სწორი იმეილი')
            # raise ValueError('Users must have a valid email address.')

        account = self.model(
            email=self.normalize_email(email)
        )

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs)
        account.is_staff = True
        account.is_admin = True
        account.is_active = True
        account.is_superuser = True
        account.save()

        return account





class Account(AbstractBaseUser, PermissionsMixin):


    ASC = (
    ("0", _("-----")),
    ("1", _("მამრობითი")),
    ("2", _("მდედრობითი")),
    )
    first_name = models.CharField(verbose_name=_("სახელი"),max_length=40, blank=True)
    last_name = models.CharField(verbose_name=_("გვარი"),max_length=40, blank=True)
    email = models.EmailField(verbose_name=_("ემაილი"),unique=True)
    personal_number = models.IntegerField(_('პირადი ნომერი'), default=1)
    phone= models.CharField(verbose_name=_("მობ.ტელეფონი"), max_length=40, blank=True, null=True)
    rules = models.BooleanField(verbose_name=_("წესები"),default=False)
    sex = models.CharField(_("სქესი"), max_length=1, default='0', choices=ASC)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    basket = models.ForeignKey('app.BasketModel', null=True, verbose_name=_('კალათა'), blank=True)

    address = models.ManyToManyField('AddressModel', verbose_name=_('მისამართი'),blank=True)
    
    # username = models.CharField(verbose_name=_("მეტსახელი"),max_length=40, unique=True)
    # tagline = models.CharField(max_length=140, blank=True)    
    # avatar=models.ImageField(verbose_name=_("სურათი"),upload_to='myapp',default='myapp/palitra-media.jpg')
    # phone= models.CharField(verbose_name=_("მობ.ტელეფონი"), max_length=40, blank=True, null=True)
    # location = models.CharField(verbose_name=_("მდებარეობა"), max_length=40, blank=True, null=True)
    # address = models.CharField(verbose_name=_("მისამართი"), max_length=40, blank=True, null=True)
    # profession = models.CharField(verbose_name=_("პროფესია"), max_length=40, blank=True, null=True)
    # work_time = models.DateField(verbose_name=_("მუშაობის დაწყების დრო"), max_length=40, blank=True, null=True)
    # status = models.CharField(verbose_name=_("სტატუსი"), max_length=200, blank=True, null=True)
    # born = models.DateField(verbose_name=_("დაბადების თარიღი"), blank=True, null=True)
    # home_phone = models.CharField(verbose_name=_("სახ.ტელეფონი"), max_length=40, blank=True, null=True)
    # experience = models.CharField(verbose_name=_("გამოცდილება"), max_length=40, blank=True, null=True)
    objects = AccountManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['']

    def __str__(self):
        return self.first_name

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name

    # def get_profile_url(self):
    #     return "/profile/"

    class Meta:
        verbose_name = _('ექაუნთი')
        verbose_name_plural = _('ექაუნთები')

class AddressModel(models.Model):
    citychoice = (
        ('0',_('--------')),
        ('1',_('თბილისი')),
        ('2',_('ბათუმი')),
        ('3','ქუთაისი'),
        ('4','რუსთავი'),
        ('5','გორი'),
        ('6','ზუგდიდი'),
        ('7','ფოთი'),
        ('8','ხაშური'),
        ('9','სამტრედია'),
        ('10', 'სენაკი'),
        ('11', 'ზესტაფონი'),
        ('12', 'მარნეული'),
        ('13', 'თელავი'),
        ('14', 'ახალციხე'),
        ('15', 'ქობულეთი'),
        ('16', 'ოზურგეთი'),
        ('17', 'კასპი'),
        ('18', 'ჭიათურა'),
        ('19', 'წყალტუბო'),
        ('20', 'საგარეჯო'),
        ('21', 'გარდაბანი'),
        ('22', 'ბორჯომი'),
        ('23', 'ტყიბული'),
        ('25','ბოლნისი'),
        ('26', 'ახალქალაქი'),
        ('27', 'გურჯაანი'),
        ('28', 'მცხეთა'),
        ('29', 'ყვარელი'),
        ('30', 'ახმეტა'),
        ('31', 'ქარელი'),
        ('32', 'ლანჩხუთი'),
        ('33', 'დუშეთი'),
        ('34', 'საჩხერე'),
        ('35', 'დედოფლისწყარო'),
        ('36', 'ლაგოდეხი'),
        ('37', 'ნინოწმინდა'),
        ('38', 'აბაშა'),
        ('39', 'წნორი'),
        ('40', 'თერჯოლა'),
        ('41', 'მარტვილი'),
        ('42', 'ხობი'),
        ('43', 'წალენჯიხა'),   
        ('44', 'ვანი'),
        ('45', 'ბაღდათი'),
        ('46', 'ვალე'),
        ('47', 'თეთრიწყარო'), 
        ('48', 'დმანისი'),
        ('49', 'ონი'),
        ('50', 'წალკა'),
        ('51','ამბროლაური'),
        ('52', 'სიღნაღი'),
        ('53', 'ცაგერი'),
        ('54', 'ჯვარი'),
    )
    city = models.CharField(max_length=2,default = 0, choices = citychoice , verbose_name = _('ქალაქი'))
    street = models.CharField(max_length=150, default ='', verbose_name=_('ქუჩა'))
    comment = models.CharField(max_length=500 , default = '', verbose_name=_('კომენატრი'))
    user = models.CharField(max_length = 20, default= '' , verbose_name = _('პიროვნება'))

    def __str__(self):
        for city in self.citychoice:
            if city[0] == self.city:
                return city[1] +' | '+ self.street +' | '+ self.user 
    class Meta:
        verbose_name = _('მისამართი')
        verbose_name_plural = _('მისამართები')    



@receiver(post_save, sender=Account)
def p_save(sender, **kwargs):

    object = kwargs.get("instance") 
    if kwargs['created']:
        object.basket = BasketModel.objects.create()
        object.save()