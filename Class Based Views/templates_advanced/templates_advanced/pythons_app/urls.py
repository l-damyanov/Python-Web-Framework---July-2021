from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from templates_advanced.pythons_app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('create/', views.PythonCreateView.as_view(), name="create"),
]

# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
