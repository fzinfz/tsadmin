from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from markdownx.admin import MarkdownxModelAdmin
from markdownx.widgets import AdminMarkdownxWidget


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'public', 'status', 'topped']
    list_filter = ('public', 'status')
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }


class AccessoriesAdmin(admin.ModelAdmin):
    list_display = ['value', 'catalog']
    list_filter = ('catalog',)
    ordering = ['id']


admin.site.register(User, UserAdmin)
admin.site.register(Node)
admin.site.register(Connection)
admin.site.register(Post, PostAdmin)
admin.site.register(Accessories, AccessoriesAdmin)
