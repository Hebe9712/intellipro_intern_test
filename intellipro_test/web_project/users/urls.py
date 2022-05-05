"""
Urls of web project

urls:
    home: the home page.
    register: the register page.
    crud: page that displays all labels
    update_label: page that change(rename) the label
    delete_label: page that delete the label

"""
from django.urls import path
from . import views
from .views import register

urlpatterns = [
    path('', views.home, name="home"),
    path("signup/", register, name="register"),
    path('label/', views.crud, name="crud"),
    path("update/<int:pk>/", views.update_label, name="update_label"),
    path("delete/<int:pk>/", views.delete_label, name="delete_label"),
]