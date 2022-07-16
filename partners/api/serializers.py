from rest_framework import serializers

from partners.models import PartnersModel


class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnersModel
        fields = '__all__'
