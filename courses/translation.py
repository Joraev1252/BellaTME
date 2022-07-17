from modeltranslation.translator import register, TranslationOptions
from courses.models import CoursesModels


@register(CoursesModels)
class CoursesTranslationOptions(TranslationOptions):
    fields = ('title', 'body', 'image')

