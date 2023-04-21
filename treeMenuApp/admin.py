from django.contrib import admin
from treeMenuApp.models import MenuItem, Menu
# Register your models here.

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'parent')
    list_filter = ('parent',)
    search_fields = ('name', 'url')

    exclude = ('is_active', )

admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)