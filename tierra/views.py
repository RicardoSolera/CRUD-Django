from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render
from .models import tierra
from tierra.forms import tierraForm
# Create your views here.


def inicio(request):
    return render(request, 'inicio.html')

def listadoTierra(request):
    Tierras = tierra.objects.all()
    return render(request, 'TierraListado.html', {'Tierras': Tierras})

def ingresarTierra(request, template='tierraForm.html'):
    form = tierraForm()
    if request.method == "POST":
        form = tierraForm(request.POST, request.FILES)
        if form.is_valid():
         form.save()
         return render(request, 'tierraNuevo.html')
    kwvars = {
        "form": form,
    }
    return render_to_response(template, kwvars, context_instance=RequestContext(request))

def eliminarTierra(request, id_t):
    instance = get_object_or_404(tierra, id_tierra=id_t)
    instance.delete()
    Tierras = tierra.objects.all()
    return render(request, 'TierraListado.html', {'Tierras': Tierras})

def editarTierra(request, id_t):
    instance = get_object_or_404(tierra, id_tierra=id_t)
    form = tierraForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            Tierras = tierra.objects.all()
            return render(request, 'TierraListado.html', {'Tierras': Tierras})
    return render(request, 'tierraForm.html', {'form': form})
    