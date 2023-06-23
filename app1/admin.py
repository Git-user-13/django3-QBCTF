from django.contrib import admin

# Register your models here.

from . models import Product
from . models import Flag
from . models import complete
from . models import Board

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'description','created_at')

class FlagAdmin(admin.ModelAdmin):
    list_display = ('id','q1','h1','f1','score')

class completeAdmin(admin.ModelAdmin):
    list_display = ('id','user','hint','completed','finished_at')

class BoardAdmin(admin.ModelAdmin):
    list_display = ('id','user','score','finished_at')

admin.site.register(Product,ProductAdmin)
admin.site.register(Flag,FlagAdmin)
admin.site.register(complete,completeAdmin)
admin.site.register(Board,BoardAdmin)