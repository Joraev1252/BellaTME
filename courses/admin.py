from django.contrib import admin
from courses.models import CoursesModels


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'body', )
    list_filter = ('id',)


admin.site.register(CoursesModels, TodoAdmin)