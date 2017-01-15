from django.contrib import admin
from .models import BookModel , CategoryModel , SlideModel ,OrderModel ,BasketModel ,BasketLine,ReadersclubModel
# Register your models here.
admin.site.register(BookModel)
admin.site.register(CategoryModel)
admin.site.register(SlideModel)
admin.site.register(OrderModel)
admin.site.register(BasketModel)
admin.site.register(BasketLine)
admin.site.register(ReadersclubModel)