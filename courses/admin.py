from django.contrib import admin
from courses.models import CoursesModels
from modeltranslation.admin import TranslationAdmin

# class ToDoCustomAdmin(admin.ModelAdmin):
#     list_display = ('title',)
#     class Meta:
#         verbose_name = "Central-Asia"
#
# class CAPageAdmin(ToDoCustomAdmin, TranslationAdmin):
#     pass
# admin.site.register(CoursesModels, CAPageAdmin)


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'body', )
    list_filter = ('id',)


admin.site.register(CoursesModels, TodoAdmin)