from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Tarea
from .forms import TareaForm

def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'lista_tareas.html',
    {'tareas': tareas})

def nueva_tarea(request):
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm()
        return render(request, 'nueva_tarea.html', {'form':
        form})
    

def editar_tarea(request,pk):
    tarea = get_object_or_404(Tarea,pk=pk)
    if request.method == "POST":
        form = TareaForm(request.POST, instance=tarea)

        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm(instance=tarea)
        return render(request, 'editar_tarea.html', {'form':
        form, 'tarea':tarea})