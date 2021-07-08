from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('filtro_productos/<int:seccion_id>', views.filtro_productos, name="filtro_productos"),
    path('acerca', views.acerca, name="acerca"),
    path('contacto', views.contacto, name="contacto"),
    path('alta_producto', views.alta_producto, name="alta_producto"),
    path('lista_producto/<int:id>', views.lista, name='lista'),
    path('modificar/<int:id>', views.modificar_producto, name='modificar_producto'),
    path('eliminar/<int:id>', views.eliminar_producto, name='eliminar_producto'),
]