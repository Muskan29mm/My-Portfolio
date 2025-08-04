from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

# Create your views here.
def landing_page(request):
    return render(request, 'MyPortfolio/landing_page.html')

def about_me(request):
    return render(request, 'MyPortfolio/about_me_page.html')

def skills(request):
    return render(request, 'MyPortfolio/skills.html')

def projects(request):
    return render(request, 'MyPortfolio/projects.html')

def courses(request):
    return render(request, 'MyPortfolio/courses.html')

def certifications(request):
    return render(request, 'MyPortfolio/certificates.html')

def contact(request):
    return render(request, 'MyPortfolio/contact.html')

def resume(request):
    return render(request, 'MyPortfolio/resume.html')
