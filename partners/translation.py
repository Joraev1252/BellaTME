from modeltranslation.translator import register, TranslationOptions
from partners.models import PartnersModel


@register(PartnersModel)
class PartnersTranslationOptions(TranslationOptions):
    fields = ('logo', 'link')

