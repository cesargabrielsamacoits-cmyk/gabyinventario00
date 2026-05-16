from django.shortcuts import render , redirect
from actionbases.models import ActionBase
from actionbases.forms import ActionBaseForm
from django.views.generic import DetailView, UpdateView , DeleteView
from django.urls import reverse_lazy


def base_list(request):
    bases_q = ActionBase.objects.all()

    return render(
        request,
        "actionbases/base_list.html",
        {"bases": bases_q}
    )

def base_create(request):
    if request.method == "POST":
        form = ActionBaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("base_list")
    else:
        form = ActionBaseForm()
    
    return render(
        request,
        "actionbases/base_create.html",
        {"form": form}
    )
    
class ActionBaseDetailView(DetailView):
    model = ActionBase
    template_name = "actionbases/base_detail_view.html"
    context_object_name = "base"
    slug_field = "slug"
    slug_url_kwarg = "slug"


class ActionBaseUpdateView(UpdateView):
    model = ActionBase
    fields = ['nombre', 'descripcion', 'precio', 'cantidad']
    template_name = "actionbases/base_create.html"

    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_success_url(self):
        return reverse_lazy(
            'base_detail_view',
            kwargs={'slug': self.object.slug}
        )


class ActionBaseDeleteView(DeleteView):
    model = ActionBase
    template_name = "actionbases/base_confirm_delete.html"

    slug_field = "slug"
    slug_url_kwarg = "slug"

    success_url = reverse_lazy('base_list')