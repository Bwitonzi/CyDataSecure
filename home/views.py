from django.shortcuts import render

# Home view for CyDataSecure SaaS app
def home(request):
    return render(request, 'home/home.html')