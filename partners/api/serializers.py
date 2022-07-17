from rest_framework import serializers

from partners.models import PartnersModel


class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnersModel
        fields =['logo_ru', 'logo_en', 'logo_uz', 'logo_zh', 'logo_zho',
                  'link_ru', 'link_en', 'link_uz', 'link_zh', 'link_zho'
                    ]
