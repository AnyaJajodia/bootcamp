from django.urls import path
from . import views

app_name = 'contacts'
urlpatterns = [
    path('', views.index, name='contact_index'),
    path('<int:contact_id>/', views.details, name='contact_details'),
    path('create/', views.create, name='contact_create'),
    path('edit/<int:contact_id>/', views.edit, name='contact_edit'),
    path('delete/<int:contact_id>/', views.delete, name='contact_delete'),
]
