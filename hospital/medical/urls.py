from django.urls import path
from .import views

urlpatterns = [
    path('specialty_list/', views.specialty_list, name= 'specialty_list'),
    path('specialty_detail/<int:pk>', views.specialty_detail, name= 'specialty_detail'),
    path('specialty_create/', views.specialty_create, name= 'specialty_create'),
    path('specialty_edit/<int:pk>', views.specialty_edit, name= 'specialty_edit'),
    path('specialty_delete/<int:pk>', views.specialty_delete, name= 'specialty_delete'),
    path('changeStatus/<int:pk>', views.changeStatus, name= 'changeStatus'),
    
    path('doctor_list/', views.doctor_list, name= 'doctor_list'),
    path('doctor_detail/<int:pk>', views.doctor_detail, name= 'doctor_detail'),
    path('doctor_create/', views.doctor_create, name= 'doctor_create'),
    path('doctor_edit/<int:pk>', views.doctor_edit, name= 'doctor_edit'),
    path('doctor_delete/<int:pk>', views.doctor_delete, name= 'doctor_delete'),
    path('changeStatusD/<int:pk>', views.changeStatusD, name= 'changeStatusD'),
]
