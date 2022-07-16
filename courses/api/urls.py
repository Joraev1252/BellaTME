from django.urls import path, include

from courses.api.views import course_view

app_name = 'courses'

urlpatterns = [
    path('courses', course_view, name='course'),

]


