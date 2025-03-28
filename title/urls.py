from django.urls import path
from . import views

urlpatterns = [
     
     path('title/<int:main_title_id>',views.title, name='title'),
    
    
    
]