from django.shortcuts import render
from .models import Persona
from .models import TipoDocumento
from .models import Ciudad

# Create your views here.

def inicio(request):
    return render(request,'index.html')