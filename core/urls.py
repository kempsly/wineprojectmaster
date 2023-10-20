from django.urls import path
from core import views


app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about_view, name="about"),
    path("product/", views.product_view, name="product"),
    path("blog/", views.blog_view, name="blog"),
    path("contact/", views.contact_view, name="contact"),
    # path("services/", views.about, name="about"),
]
