from django.contrib import admin
from .models import Account , AddressModel


class AccountAdmin(admin.ModelAdmin):
	list_display = [  'email',  'first_name', 'last_name' ]
	search_fields = [ 'email', 'first_name',  'last_name']
					
	class Meta:
		model = Account



class AddressAdmin(admin.ModelAdmin):
	list_display = ['city',  'street' , 'user']
	search_fields = ['city',  'street','user']
					
	class Meta:
		model = AddressModel

admin.site.register(Account, AccountAdmin)

admin.site.register(AddressModel, AddressAdmin)
 

