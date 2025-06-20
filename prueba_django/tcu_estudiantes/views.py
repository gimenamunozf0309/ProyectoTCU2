import requests
from django.conf import settings
from django.shortcuts import render
from .forms import TCUEstudianteForm

def registrar_tcu(request):
    if request.method == "POST":
        form = TCUEstudianteForm(request.POST, request.FILES)
        if form.is_valid():
            estudiante = form.save()  # Guarda en Django

            # 🔹 Enviar datos a Odoo
            url = f"{settings.ODOO_URL}/api/tcu_estudiante"
            auth = (settings.ODOO_USERNAME, settings.ODOO_PASSWORD)
            data = {
                "nombre": estudiante.nombre,
                "identificacion": estudiante.identificacion,
                "carnet": estudiante.carnet,
                "correo": estudiante.correo,
                "telefono": estudiante.telefono,
                "periodo_tcu": estudiante.periodo_tcu.nombre,  # 🔹 Enviar nombre del período
                "estado": estudiante.estado,
            }

            response = requests.post(url, json=data, auth=auth)

            # 🔹 Imprimir la respuesta en la terminal para verificar errores
            print("🔹 Respuesta de Odoo:", response.status_code, response.text)

    else:
        form = TCUEstudianteForm()

    return render(request, "tcu_estudiantes/registrar_tcu.html", {"form": form})

