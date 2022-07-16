from rest_framework import serializers
from free_lesson.models import FreeLessonModel


class FreeLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeLessonModel
        fields = "__all__"
