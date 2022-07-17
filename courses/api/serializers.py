from rest_framework import serializers

from courses.models import CoursesModels


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursesModels
        fields = ['title_ru', 'title_en', 'title_uz', 'title_zh', 'title_zho',
                  'body_ru', 'body_en', 'body_uz', 'body_zh', 'body_zho',
                  'image_ru', 'image_en', 'image_uz', 'image_zh', 'image_zho'
                  ]



