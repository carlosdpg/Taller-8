from django.shortcuts import render
from .models import Persona
from .models import TipoDocumento
from .models import Ciudad

# Create your views here.

def get_data_for_columns(request):
    column_personas = Persona.objects.all()
    column_tiposdocumentos = TipoDocumento.objects.all()
    column_ciudades = Ciudad.objects.all()

    context = {
        'personas': column_personas,
        'tiposdocumentos': column_tiposdocumentos,
        'ciudades': column_ciudades
    }
    
    return render(request, 'index.html', context)