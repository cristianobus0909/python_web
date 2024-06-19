from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def index(req):
    return render(req,'index.html',{})
def cursos(req):
    cursos = Curso.objects.all()
    return render(req,'cursos.html',{"cursos":cursos})
def cursos_formulario(req):
    if req.method == "POST":
        miFormulario = CursoFormulario(req.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion['curso'],camada=informacion['camada'])
            curso.save()       
            return render(req,'index.html',{})
    else:
        miFormulario= CursoFormulario()
    return render(req,'curso_formulario.html',{'miFormulario':miFormulario})

def estudiantes(req):
    return render(req,'estudiantes.html',{})
def profesores(req):
    return render(req,'profesores.html',{})
def profesor_formulario(req):
    if req.method == "POST":
        miFormulario = ProfesorFormulario(req.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'],apellido=informacion['apellido'],email=informacion['email'],profesion=informacion['profesion'])
            profesor.save()       
            return render(req,'index.html',{})
    else:
        miFormulario= ProfesorFormulario()
    return render(req,'curso_formulario.html',{'miFormulario':miFormulario})
def busquedaCamada(req):
    return render(req,'busquedaCamada.html',{})
def buscar(req):
    if  req.GET['camada']:
        camada = req.GET['camada']
        cursos = Curso.objects.filter(camada_icontains=camada)

        return render(req, 'resultadoBusqueda.html',{'cursos':cursos,'camada':camada})
    else:
        respuesta = 'No enviaste datos'
    return render(req,'buscar.html',{respuesta})
