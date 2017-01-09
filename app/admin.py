from django.contrib import admin
from .models import BookModel , CategoryModel
# Register your models here.
admin.site.register(BookModel)
admin.site.register(CategoryModel)

