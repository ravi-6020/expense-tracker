from django.contrib import admin
from django.urls import path,include
from home import views
# from .views import SignUpView
from . views import *
urlpatterns = [
    path('', views.home ,name="home"),
    # path('index', views.index, name="index"),
    path('login', views.loginuser, name="login"),
    path('logout', views.logoutuser, name="logout"),
    path("signup", views.signupview, name="signup"),
    # path("signup/", SignUpView.as_view(), name="signup"),
]