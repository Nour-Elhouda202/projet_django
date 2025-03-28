from django.urls import path
from . import views

urlpatterns = [
    path('subtitle/<int:subtitle_id>/', views.subtitle, name='subtitle'),
]