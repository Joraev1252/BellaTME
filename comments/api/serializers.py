from rest_framework import serializers

from comments.models import CommentsModel


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentsModel
        fields = '__all__'



