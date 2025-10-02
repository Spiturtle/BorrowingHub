from django.urls import path
from . import views

app_name = 'landing_app'

urlpatterns = [
    path('', views.landing, name='landing'),
]
