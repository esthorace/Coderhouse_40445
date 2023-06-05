from typing import Any, Dict

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from . import forms, models


class VentaDetail(DetailView):
    model = models.Venta


class VentaList(ListView):
    model = models.Venta

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.Venta.objects.filter(nombre__icontains=query)
        else:
            object_list = models.Venta.objects.all()
        return object_list


class VentaCreate(CreateView):
    model = models.Venta
    form_class = forms.VentaForm
    success_url = reverse_lazy("venta:index")

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["usuario"] = self.request.user
        return super().get_context_data(**kwargs)


class VentaDelete(DeleteView):
    model = models.Venta
    success_url = reverse_lazy("venta:venta_list")


class VentaUpdate(UpdateView):
    model = models.Venta
    success_url = reverse_lazy("venta:venta_list")
    form_class = forms.VentaForm
