from django.http import HttpResponse
from django.shortcuts import render
from familiar.models import Familiar


def padre(self):

    padre = Familiar(nombre="Luis", edad="24", fecha_nac="1971-08-12")
    padre.save()

    ret = f"Soy el padre de la familia, mi nombre es {padre.nombre}, nací el {padre.fecha_nac} y tengo {padre.edad} años."

    return HttpResponse(ret)


def madre(self):

    madre = Familiar(nombre="Monica", edad="49", fecha_nac="1973-01-23")
    madre.save()

    ret = f"Soy la madre de la familia, mi nombre es {madre.nombre}, nací el {madre.fecha_nac} y tengo {madre.edad} años."

    return HttpResponse(ret)


def hijo(self):

    hijo = Familiar(nombre="Brahyam", edad="23", fecha_nac="1998-01-23")
    hijo.save()

    ret = f"Soy el hijo mayor de la familia, mi nombre es {hijo.nombre}, nací el {hijo.fecha_nac} y tengo {hijo.edad} años."

    return HttpResponse(ret)
