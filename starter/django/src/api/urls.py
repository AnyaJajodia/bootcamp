from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from .views import contact_list, contact_details


app_name = 'api'

urlpatterns = [
    path('contact/', contact_list, name='contact_list'),
    # path('contact/<int:contact_id>/', contact_details, name='contact_details'),
]
