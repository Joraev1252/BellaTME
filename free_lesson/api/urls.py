from django.urls import path
from free_lesson.api.views import *


app_name = 'lesson_api'

urlpatterns = [
    path('post_data', post_data),
]
