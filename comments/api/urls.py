from django.urls import path, include

from comments.api.views import comments_view

app_name = 'comments'

urlpatterns = [
    path('comments', comments_view, name='course'),

]