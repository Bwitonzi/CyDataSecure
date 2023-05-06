from django.shortcuts import render

def introduction_to_cybersecurity(request):
    return render(request, 'cytraining/introduction_to_cybersecurity.html')

def introduction_to_cybersecurity2(request):
    return render(request, 'cytraining/introduction_to_cybersecurity2.html')