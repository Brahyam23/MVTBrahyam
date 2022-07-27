from django.http import HttpResponse
from familiar.models import Familiar
from django.template import Template, Context, loader


def padre(self):

    padre = Familiar(nombre="Luis", edad="51", fecha_nac="1971-08-12")
    padre.save()

    datos = {"nombre": padre.nombre, "edad": padre.edad,
             "fecha_nac": padre.fecha_nac}

    plantilla = loader.get_template("padre.html")

    documento = plantilla.render(datos)

    return HttpResponse(documento)


def madre(self):

    madre = Familiar(nombre="Monica", edad="49", fecha_nac="1973-01-23")
    madre.save()

    datos = {"nombre": madre.nombre, "edad": madre.edad,
             "fecha_nac": madre.fecha_nac}

    plantilla = loader.get_template("madre.html")

    documento = plantilla.render(datos)

    return HttpResponse(documento)


def hijo(self):

    hijo = Familiar(nombre="Brahyam", edad="23", fecha_nac="1998-01-23")
    hijo.save()

    datos = {"nombre": hijo.nombre, "edad": hijo.edad,
             "fecha_nac": hijo.fecha_nac}

    plantilla = loader.get_template("hijo.html")

    documento = plantilla.render(datos)

    return HttpResponse(documento)
