"""djangoforum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .views import home_view, user_login_view, user_logout_view, user_register_view, edit_profile_view

from django.contrib.auth import views as auth_views

from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home_view'),
    path('login/', user_login_view, name='user_login_view'),
    path('logout/', user_logout_view, name='user_logout_view'),
    path('register/', user_register_view, name='user_register_view'),
    path('forum/', include('simpleforum.urls')),

    path('edit_profile/', edit_profile_view, name='edit_profile_view'),

    # TODO password reset names and routing are fixed
    path('reset_password/', auth_views.PasswordResetView.as_view() , name='reset_password'),
    # path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done' ),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm' ),
    # path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view() , name='password_reset_complete' ),

]