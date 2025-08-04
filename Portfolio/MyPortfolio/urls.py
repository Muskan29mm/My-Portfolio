from . import views
from django.urls import path



urlpatterns = [
    path("", views.landing_page, name="landing_page"),
    path('', views.landing_page, name='home'),
    path('about/', views.about_me, name='about'),
    path('skills/', views.skills, name='skills'),
    path('projects/', views.projects, name='projects'),
    path('certificates/', views.certifications, name='certificates'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.courses, name='courses'),
    path('resume/', views.resume, name='resume'),
]