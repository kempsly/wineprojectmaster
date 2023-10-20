from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def home(request):
    
    return render(request, 'core/index.html')

def about_view(request):
    return render(request, 'core/about.html')

def product_view(request):
    return render(request, 'core/product.html')

def blog_view(request):
    return render(request, 'core/blog.html')


def services_view(request):
    return render(request, 'core/services.html')

def contact_view(request):
    return render(request, 'core/contact.html')