from django.shortcuts import render, redirect
from .models import Evento, Participante
from .forms import EventoForm, ParticipanteForm
from django.contrib import messages

def inicio(request):
    return render(request, 'inicio.html')


# Vista para los formularios
def registro(request):
    if request.method == 'POST':
        evento_form = EventoForm(request.POST)
        participante_form = ParticipanteForm(request.POST)

        if evento_form.is_valid() and participante_form.is_valid():
            # Guardar evento
            evento = evento_form.save()

            # Crear participante, asignarle evento y guardar
            participante = participante_form.save(commit=False)
            participante.evento = evento
            participante.save()

            # Mensaje de éxito
            messages.success(request, f"✅ El evento '{evento.nombre}' fue registrado con éxito junto al participante {participante.nombre}.")
            return redirect('confirmacion')
        else:
            # Mensajes de error
            messages.error(request, "⚠️ Revisa los errores en los formularios antes de continuar.")

    else:
        evento_form = EventoForm()
        participante_form = ParticipanteForm()

    return render(request, 'registro.html', {
        'evento_form': evento_form,
        'participante_form': participante_form
    })


# Vista mensaje confirmación
def confirmacion(request):
    return render(request, 'confirmacion.html')

def contacto(request):
    return render(request, 'contacto.html')
