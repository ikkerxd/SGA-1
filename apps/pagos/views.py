from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin
from django.core.urlresolvers import reverse_lazy

from .forms import DescuentoForm, EstructuraPagosForm, PagoForm
from .models import Descuento, Estructura_Pago

from apps.matricula.models import Matricula

from django.utils import timezone


class DescuentoView(TemplateView):
    template_name = 'mantenimientos/descuento/panel_descuento.html'

    def get_context_data(self, **kwargs):
        context = super(DescuentoView, self).get_context_data(**kwargs)
        context['descuentos'] = Descuento.objects.all()
        context['cantidad'] = context['descuentos'].count()
        return context


class DetalleDescuento(DetailView):
    template_name = 'mantenimientos/descuento/detalle_descuento.html'
    model = Descuento


class AgregarDescuento(CreateView):
    form_class = DescuentoForm
    template_name = 'mantenimientos/descuento/agregar_descuento.html'
    success_url = reverse_lazy('pagos_app:panel_descuento')


class ModificarDescuento(UpdateView):
    model = Descuento
    template_name = 'mantenimientos/descuento/modificar_descuento.html'
    success_url = reverse_lazy('pagos_app:panel_descuento')
    form_class = DescuentoForm


class EliminarDescuento(DeleteView):
    template_name = 'mantenimientos/descuento/eliminar_descuento.html'
    model = Descuento
    success_url = reverse_lazy('pagos_app:panel_descuento')


class EstructurapagoView(TemplateView):
    template_name = 'mantenimientos/estructurapagos/panel_estructurapagos.html'

    def get_context_data(self, **kwargs):
        context = super(EstructurapagoView, self).get_context_data(**kwargs)
        context['EstructuraPagos'] = Estructura_Pago.objects.all()
        context['cantidad'] = context['EstructuraPagos'].count()
        return context


class DetalleEstructuraPagos(DetailView):
    template_name = 'mantenimientos/estructurapagos/detalle_estructurapagos.html'
    model = Estructura_Pago


class AgregarEstructuraPagos(CreateView):
    form_class = EstructuraPagosForm
    template_name = 'mantenimientos/estructurapagos/agregar_estructurapagos.html'
    success_url = reverse_lazy('pagos_app:panel_estructurapagos')


class ModificarEstructuraPagos(UpdateView):
    model = Estructura_Pago
    template_name = 'mantenimientos/estructurapagos/modificar_estructurapagos.html'
    success_url = reverse_lazy('pagos_app:panel_estructurapagos')
    form_class = EstructuraPagosForm


class EliminarEstructuraPagos(DeleteView):
    template_name = 'mantenimientos/estructurapagos/eliminar_estructurapagos.html'
    model = Estructura_Pago
    success_url = reverse_lazy('pagos_app:panel_estructurapagos')


class PanelCajaView(TemplateView):
    template_name = 'panel_caja/panel.html'


class MatriculaPendiente(ListView):

    template_name = 'procesos/pagos/matricula/lista_matricula.html'
    paginate_by = 2

    def get_queryset(self):
        # se crea la variable objeto
        self.matriculados = Matricula.objects.matricula_pendiente()
        return self.matriculados

    def get_context_data(self, **kwargs):
        # Llama primero a la implementacion para traer el contexto
        context = super(MatriculaPendiente, self).get_context_data(**kwargs)
        context['cantidad'] = self.matriculados.count()
        return context


class RegistrarPago(FormMixin, DetailView):
    model = Matricula
    form_class = PagoForm
    template_name = 'procesos/pagos/matricula/pago_matricula.html'

    def get_success_url(self):
        return reverse_lazy('pagos_apps:matricula_pendiente')

    def get_context_data(self, **kwargs):
        context = super(RegistrarPago, self).get_context_data(**kwargs)
        # self.get_form() es form_class enviamos el formulario {{ form }}
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        # get_object() es el parametro matricula q se psa por url
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        
        concepto = '1'
        monto = form.cleaned_data['monto']        
        fecha = timezone.now()
        matricula = self.object

        aportacion = Aportacion(
            concepto=concepto,
            monto=monto,
            fecha_pago=fecha,
            matricula=matricula
        )

        tipo = form.cleaned_data['tipo']
        serie = form.cleaned_data['serie']
        numero = form.cleaned_data['numero']

        descuento =form.cleaned_data['descuento']
        monto_descuento = monto*descuento.porcentaje/100.0
        sub_total = monto - monto_descuento

        comprabante = Comprobante(
            tipo=tipo,
            serie=serie,
            numero=numero,
            
        )




        print monto
        print fecha
        print matricula
        print porcentaje
        print monto_descuento
        print sub_total
        return super(RegistrarPago, self).form_valid(form)
