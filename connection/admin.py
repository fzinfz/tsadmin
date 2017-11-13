from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from markdownx.admin import MarkdownxModelAdmin
from markdownx.widgets import AdminMarkdownxWidget


def mark_outdated(modeladmin, request, queryset):
    queryset.update(status="OUTDATED")
    mark_outdated.short_description = "Mark Outdated"


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'slug', 'public', 'list', 'status', 'topped']
    list_filter = ('public', 'list', 'status')
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }
    actions = [mark_outdated]


class AccessoriesAdmin(admin.ModelAdmin):
    list_display = ['value', 'catalog']
    list_filter = ('catalog',)
    ordering = ['-catalog','value']


class ConnectionAdmin(admin.ModelAdmin):
    list_display = ['port', 'user', 'protocol', 'method', 'due_date']
    list_filter = ('protocol',)
    ordering = ['port']


class NodeAdmin(admin.ModelAdmin):
    list_display = ['domain_name', 'location', 'status', 'traffic_rate', 'sort']
    list_filter = ('status',)
    ordering = ['sort']


class CustomUserAdmin(UserAdmin):
    def __init__(self, *args, **kwargs):
        super(UserAdmin, self).__init__(*args, **kwargs)
        UserAdmin.list_display = \
            ['username', 'email', 'is_superuser', 'nickname', 'aff_code', 'aff_by']


admin.site.register(User, CustomUserAdmin)
admin.site.register(Node, NodeAdmin)
admin.site.register(Connection, ConnectionAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Accessories, AccessoriesAdmin)
