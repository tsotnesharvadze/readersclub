from django.contrib import admin
from .models import BookModel , CategoryModel , SlideModel
# Register your models here.
admin.site.register(BookModel)
admin.site.register(CategoryModel)
admin.site.register(SlideModel)
