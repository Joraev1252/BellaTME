from django.contrib import admin
from partners.models import PartnersModel


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'link', )
    list_display_links = ('id', 'link', )
    search_fields = ('id', )
    list_filter = ('id',)


admin.site.register(PartnersModel, TodoAdmin)