from django.urls import path

from partners.api.views import partners_view

app_name = 'partners'

urlpatterns = [
    path('partners', partners_view, name='partners'),


]