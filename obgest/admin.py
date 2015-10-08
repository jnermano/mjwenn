from django.contrib import admin

from . import models
# Register your models here.
class TypeInline(admin.TabularInline):
    model = models.Type
    extra = 3

class CategoryAdmin(admin.ModelAdmin):
    inlines = [TypeInline]
    list_display = ('category', 'desc')
    
class TypeAdmin(admin.ModelAdmin):
    fields = ['category', 'type', 'desc']
    list_display = ('category', 'type', 'desc')

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Type, TypeAdmin)