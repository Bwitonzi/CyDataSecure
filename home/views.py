from django.shortcuts import render

# Home view for CyDataSecure SaaS app
def home(request):
    return render(request, 'home/home.html')

# Homepage1 view for CyDataSecure SaaS app
def homepage1(request):
    return render(request, 'home/hompepage1.html')

# Homepage2 view for CyDataSecure SaaS app
def homepage2(request):
    return render(request, 'home/homepage2.html')