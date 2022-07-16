from django.contrib import admin
from free_lesson.models import FreeLessonModel


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'age', 'phone_number', 'email', 'level', 'sex')
    list_filter = ('id',)


admin.site.register(FreeLessonModel, TodoAdmin)
