from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', redirect_authenticated_user=True), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', SignUp.as_view(), name='signup'),
    path('password-reset/', Reset_Password_View.as_view(
        template_name='accounts/password_reset.html'), name='password reset'),
]
