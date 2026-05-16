from django.shortcuts import render , redirect
#from django.http import HttpResponse
from inventario.models import ModelKit
from inventario.forms import ModelKitForm
from django.views.generic import ListView, DetailView, UpdateView , DeleteView
from django.urls import reverse_lazy


def index(request):
    return render(request, "inventario/index.html")
    #return HttpResponse("Funciona!")


def modelkit_list(request):
    modelkits_q = ModelKit.objects.all() #es una consulta a la base de datos para obtener todos los objetos de la clase ModelKit
    return render(request, "inventario/modelkit_list.html", {"modelkits": modelkits_q})

def agregar_modelkit(request):
    if request.method == "POST":
        form = ModelKitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('modelkit_list')
    else:
        form = ModelKitForm()
        
    return render(request, "inventario/agregar_modelkit.html", {"form": form})



class ModelKitListView(ListView):
    model = ModelKit
    template_name = "inventario/modelkit_list.html"
    context_object_name = "modelkits"
    
    
class ModelKitDetailView(DetailView):
    model = ModelKit
    template_name = "inventario/modelkit_detail_view.html"
    context_object_name = "modelkit"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    
    
class ModelKitUpdateView(UpdateView):
    model = ModelKit
    fields = [
        'nombre',
        'descripcion',
        'grado',
        'escala',
        'precio',
        'cantidad'
    ]

    template_name = "inventario/agregar_modelkit.html"

    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_success_url(self):
        return reverse_lazy(
            'modelkit_detail_view',
            kwargs={'slug': self.object.slug}
        )


class ModelKitDeleteView(DeleteView):
    model = ModelKit
    template_name = "inventario/modelkit_confirm_delete.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    success_url = reverse_lazy('modelkit_list')
    
