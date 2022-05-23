from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home, name="home"),
    path('contact.html',views.contact, name="contact"),
    path('about.html',views.about, name="about"),
    path('blog.html',views.blog, name="blog"),
    path('service.html',views.service, name="service"),
    path('implant.html',views.implant, name="implant"),
    path('g_dentistry.html',views.g_dentistry, name="g_dentistry"),
    path('blog_details.html', views.blog_details, name='blog_details'),
    path('appointment.html',views.appointment, name="appointment"),
    
    path('videos.html', views.videos, name='videos'),
    path('dentists.html', views.dentists, name='dentists'),
    
]
