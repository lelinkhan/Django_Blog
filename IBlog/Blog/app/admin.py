from django.contrib import admin
from . models import *

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','url','image_tag','add_date']
    list_filter = ('title','add_date')
    search_fields = ('title',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','content','url','image_tag','cat']
    list_filter = ('title','cat')
    search_fields = ('title','cat')
