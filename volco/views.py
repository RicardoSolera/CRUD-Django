from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render
from .models import volco
from volco.forms import volcoForm
# Create your views here.

def listadoVolco(request):
    Volcos = volco.objects.all()
    return render(request, 'VolcoListado.html', {'Volcos': Volcos})

def ingresarVolco(request, template='volcoForm.html'):
    form = volcoForm()
    if request.method == "POST":
        form = volcoForm(request.POST, request.FILES)
        if form.is_valid():
         form.save()
         return render(request, 'volcoNuevo.html')
    kwvars = {
        "form": form,
    }
    return render_to_response(template, kwvars, context_instance=RequestContext(request))

def eliminarVolco(request, id_v):
    instance = get_object_or_404(volco, id_volco=id_v)
    instance.delete()
    Volcos = volco.objects.all()
    return render(request, 'VolcoListado.html', {'Volcos': Volcos})

def editarVolco(request, id_v):
    instance = get_object_or_404(volco, id_volco=id_v)
    form = volcoForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            Volcos = volco.objects.all()
            return render(request, 'VolcoListado.html', {'Volcos': Volcos})
    return render(request, 'volcoForm.html', {'form': form})