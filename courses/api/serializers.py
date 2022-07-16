from rest_framework import serializers

from courses.models import CoursesModels


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursesModels
        fields = '__all__'



