from django.urls import path

from templates_advanced.pythons_app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create")
]
