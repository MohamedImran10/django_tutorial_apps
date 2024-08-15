from django.urls import path
from . import views

urlpatterns = [
    path('', views.str_con_view, name='str_con_view'),
    path('quit/', views.quit_view, name='quit_view'),
]
