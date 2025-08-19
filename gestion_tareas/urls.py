
from django.urls import path
from .views import lista_tareas, nueva_tarea,editar_tarea

urlpatterns = [
    path("lista_tareas/", lista_tareas , name="lista_tareas"),
    path("nueva_tarea/", nueva_tarea , name="nueva_tarea"),
    path("editar_tarea/<int:pk>", editar_tarea , name="editar_tarea"),
]
