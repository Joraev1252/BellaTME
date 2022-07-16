from django.contrib import admin
from comments.models import CommentsModel


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'rating', )
    list_display_links = ('id', 'user_name')
    search_fields = ('id', 'user_name', )
    list_filter = ('id',)


admin.site.register(CommentsModel, TodoAdmin)