from django.contrib import admin
from .models import *



from django.contrib import admin
from .models import *


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'languages', 'active')


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'categories', 'languages', 'title', 'header_title', 'text', 'add_date', 'edit_date', 'active')


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'order_num', 'active')


admin.site.register(Language, LanguageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Image, ImageAdmin)