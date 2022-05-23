from django.urls import path
from . import views
urlpatterns = [
    
    path('photos.html',views.photos, name='photos'),
   
]