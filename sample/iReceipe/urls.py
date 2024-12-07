from django.urls import path
from iReceipe import views

urlpatterns = [
    path("receipe", views.receipies, name="receipies"),
    
]