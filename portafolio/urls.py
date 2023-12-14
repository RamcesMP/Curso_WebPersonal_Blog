from django.urls import path,include
from .views import portafolio

urlpatterns = [
    path('', portafolio , name="portafolio")
    
]
