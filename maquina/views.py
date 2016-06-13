from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render
from .models import maquina
from maquina.forms import maquinaForm
# Create your views here.

def listadoMaquina(request):
    Maquinas = maquina.objects.all()
    return render(request, 'MaquinaListado.html', {'Maquinas': Maquinas})

def ingresarMaquina(request, template='maquinaForm.html'):
    form = maquinaForm()
    if request.method == "POST":
        form = maquinaForm(request.POST, request.FILES)
        if form.is_valid():
         form.save()
         return render(request, 'maquinaNuevo.html')
    kwvars = {
        "form": form,
    }
    return render_to_response(template, kwvars, context_instance=RequestContext(request))

def eliminarMaquina(request, id_v):
    instance = get_object_or_404(maquina, id_maquina=id_m)
    instance.delete()
    Maquinas = maquina.objects.all()
    return render(request, 'MaquinaListado.html', {'Maquinas': Maquinas})

def editarMaquina(request, id_m):
    instance = get_object_or_404(maquina, id_maquina=id_m)
    form = maquinaForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            Maquinas = maquina.objects.all()
            return render(request, 'MaquinaListado.html', {'Maquinas': Maquinas})
    return render(request, 'maquinaForm.html', {'form': form})