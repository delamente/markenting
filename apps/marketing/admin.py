from adminsortable.admin import NonSortableParentAdmin, SortableStackedInline

from django.contrib import admin

from .models import Contact, Service


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    fields = ('name', 'created_at', 'email_or_phone', 'message')
    readonly_fields = ('name', 'created_at', 'email_or_phone', 'message')
    list_display = ('name', 'created_at', 'message')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass
