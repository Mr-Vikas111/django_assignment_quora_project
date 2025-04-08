
from django.urls import path
from . import views

urlpatterns = [
    # user register view
    path("register/",views.user_register,name="_register"),
    # user login view
    path("login/",views.user_login,name="_login"),
    # user logout view
    path("logout/",views.user_logout,name="_logout"),
]
