from django.urls import path
from classificator import views

app_name = "classificator"

urlpatterns = [
    path('model/', views.handler_view, name="model-handler"),

]
