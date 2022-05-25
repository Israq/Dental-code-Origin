from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home, name="home"),
    path('contact.html',views.contact, name="contact"),
    path('about.html',views.about, name="about"),
    path('blog.html',views.blog, name="blog"),
    path('service.html',views.service, name="service"),
    path('implant.html',views.implant, name="implant"),
    path('implant2.html',views.implant2, name="implant2"),
    path('g_dentistry.html',views.g_dentistry, name="g_dentistry"),
    path('blog_details.html', views.blog_details, name='blog_details'),
    path('appointment.html',views.appointment, name="appointment"),
    path('ddetails1.html', views.ddetails1, name='ddetails1'),
    path('ddetails2.html', views.ddetails2, name='ddetails2'),
    path('ddetails3.html', views.ddetails3, name='ddetails3'),
    path('ddetails4.html', views.ddetails4, name='ddetails4'),
    path('ddetails5.html', views.ddetails5, name='ddetails5'),
    path('ddetails1.html', views.ddetails1, name='ddetails1'),
    path('videos.html', views.videos, name='videos'),
    path('dentists.html', views.dentists, name='dentists'),
    
]
