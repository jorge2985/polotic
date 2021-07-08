from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, request, HttpResponseRedirect
from .models import Categoria, Producto
from .forms import FormProductoCustom
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

# Create your views here.

def index(request):
    return render(request, 'plantillas/inicio.html', {
        "producto": Producto.objects.all()
    })

def lista(request, id):
    producto = Producto.objects.get(id=id)
    return render(request, 'plantillas/lista.html', {
        "producto": producto
    })

def acerca(request):
    return render(request, 'plantillas/acerca.html')

def contacto(request):
    return render(request, 'plantillas/contacto.html')

# Configuración de la vista del formulario
@permission_required('vendedor.add_producto')
def alta_producto(request):
    form = FormProductoCustom(request.POST or None)
    if request.method == 'POST':
        form = FormProductoCustom(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'plantillas/inicio.html', {
            "producto": Producto.objects.all()
        })
    else:
        form = FormProductoCustom()
        return render(request, 'plantillas/alta_producto.html', {
            'form': form
        })

@permission_required('vendedor.change_producto')
def modificar_producto(request, id): #id es la misma variable que se define en urls.py de la app
    un_producto = get_object_or_404(Producto, id=id)

    if request.method == "POST":
        form = FormProductoCustom(request.POST, instance = un_producto)
        if form.is_valid():
            form.save()
            return render(request, "plantillas/inicio.html", {
                "producto": Producto.objects.all()
            })
    else:
        form = FormProductoCustom(instance = un_producto)
        return render(request, 'plantillas/modificar_producto.html', {
            "un_producto": un_producto,
            "form": form
        })

@permission_required('vendedor.delete_producto')
def eliminar_producto(request, id):
    un_producto = get_object_or_404(Producto, id=id)
    un_producto.delete()
    return render(request, 'plantillas/inicio.html', {
        "producto": Producto.objects.all()
    })

def filtro_productos(request, seccion_id):
    una_categoria = get_object_or_404(Categoria, id=seccion_id)
    queryset = Categoria.objects.all()
    queryset = queryset.filter(categoria=una_categoria)
    return render(request,"plantillas/inicio.html", {
        "lista_articulos": queryset,
        "lista_categoria": Categoria.objects.all(),
        "categoria_seleccionada": una_categoria
    })