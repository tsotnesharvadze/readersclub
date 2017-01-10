from django.contrib import admin
from .models import Account


class AccountAdmin(admin.ModelAdmin):
	list_display = [  'email',  'first_name', 'last_name' ]
	search_fields = [ 'email', 'first_name',  'last_name']
					
	class Meta:
		model = Account


admin.site.register(Account, AccountAdmin)


 

