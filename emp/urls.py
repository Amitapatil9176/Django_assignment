from django.urls import path
from . import views
urlpatterns = [
    path('', views.office_list, name='office_list'),
    path('add/', views.add_office, name='add_office'),
    path('<int:pk>/', views.office_detail, name='office_detail'),
    path('<int:pk>/edit/', views.edit_office, name='edit_office'),
    path('<int:pk>/delete/', views.delete_office, name='delete_office'),
]
