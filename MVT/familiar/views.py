from django.http import HttpResponse
from django.shortcuts import render
from familiar.models import Familiar


def padre(self):

    padre = Familiar(nombre="Luis", edad="24", fecha_nac="1971-08-12")
    padre.save()

    ret = f"Soy el padre de la familia, mi nombre es {padre.nombre}, nací el {padre.fecha_nac} y tengo {padre.edad} años."

    return HttpResponse(ret)
