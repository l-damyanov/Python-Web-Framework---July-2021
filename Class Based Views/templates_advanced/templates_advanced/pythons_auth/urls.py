from django.urls import path

from templates_advanced.pythons_auth import views

urlpatterns = [
    path('sign_up/', views.SignUpView.as_view(), name='sign up'),
    path('sign_in/', views.SignInView.as_view(), name='sign in'),
    path('sign_out/', views.sign_out, name='sign out'),
]
