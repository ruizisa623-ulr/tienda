from django.shortcuts import render
from .models import Categoria

def crear(request):
    if request.method == "POST":
        categoria = Categoria(
            nombre=request.POST["nombre"],
            observaciones=request.POST["observaciones"]
        )

        categoria.save()

    return render(request, "categoria/formulario.html")


def listar(request):
    categorias = Categoria.objects.all()

    return render(request, "categoria/listar.html", {"categorias": categorias})

def detalle(request, id):
    categoria = Categoria.objects.get(id=id)

    return render(request, "categoria/detalle.html", {"categoria": categoria})

def editar(request, id):
    categoria = Categoria.objects.get(id=id)

    if request.method == "POST":
        categoria.nombre = request.POST["nombre"]
        categoria.observaciones = request.POST["observaciones"]

        categoria.save()

        return render(request, "categoria/detalle.html", {"categoria": categoria})

    return render(request, "categoria/formulario.html", {"categoria": categoria})

def eliminar(request, id):
    categoria = Categoria.objects.get(id=id)

    categoria.delete()

    return render(request, "categoria/listar.html", {"categorias": Categoria.objects.all()})
