from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from templates_advanced.pythons_app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('sign_in/', views.sign_in, name='sign in'),
    path('sign_out/', views.sign_out, name='sign out')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
