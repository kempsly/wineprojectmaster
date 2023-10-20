from django.urls import path
from userauths import views


app_name = "userauths"



urlpatterns = [
    path('sign-up/', views.register_view, name="register"),
    path('sign-in/', views.login_view, name="login"),
    # path('sign-out/', views.logout_view, name="sign-out"),
]
