from django.shortcuts import render
from .models import Project

# Create your views here.


def portafolio(request):
    proyectos=Project.objects.all()
    data={
        "proyectos":proyectos,
    }
    return render(request,"portafolio/portafolio.html",data)

   