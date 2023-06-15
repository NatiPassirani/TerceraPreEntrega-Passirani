from django.shortcuts import render


# Create your views here.
from django.shortcuts import render
from .models import Capacitacion, Contacto, Suscripcion

def insertar_datos(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        titulo = request.POST['titulo']
        descripcion = request.POST['descripcion']
        nombre = request.POST['nombre']
        email = request.POST['email']
        mensaje = request.POST['mensaje']
        suscripcion_email = request.POST['suscripcion_email']

        # Crear nuevas instancias de los modelos y guardar en la base de datos
        capacitacion = Capacitacion.objects.create(titulo=titulo, descripcion=descripcion)
        contacto = Contacto.objects.create(nombre=nombre, email=email, mensaje=mensaje)
        suscripcion = Suscripcion.objects.create(email=suscripcion_email)

        # Realizar alguna acción adicional si es necesario

    return render(request, 'insertar_datos.html')

def buscar_datos(request):
    if request.method == 'POST':
        # Obtener el término de búsqueda
        termino = request.POST['termino']

        # Realizar la búsqueda en la base de datos
        resultados_capacitacion = Capacitacion.objects.filter(titulo__icontains=termino)
        resultados_contacto = Contacto.objects.filter(nombre__icontains=termino)
        resultados_suscripcion = Suscripcion.objects.filter(email__icontains=termino)

        # Realizar alguna acción adicional si es necesario

    return render(request, 'buscar_datos.html')
