from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import Subir
from .models import GaleriaBD

# Create your views here.
def galeria(request) :
    ft = GaleriaBD.objects.all()
    contexto = {'ft': ft}
    return render(request,'galeria.html', contexto)
@login_required(login_url='logar')
def galeria_subir(request):
    form = Subir(request.POST,request.FILES )
    if request.FILES and request.POST :
        img = request.FILES.get('img')
        torpedo = GaleriaBD.objects.create(imagens=img)
        torpedo.save()
        return redirect('galeria')
    contexto = {
        'form' : form,
    }
    return render(request,'formulario.html',contexto)
@login_required(login_url='logar')
def apagar (request,pk):
    ft = GaleriaBD.objects.all()
    contexto = {
        'ft': ft,

    }
    print('cont', contexto)

    return render(request, 'del.html', contexto)
@login_required(login_url='logar')
def deletar(request,pk):
    ft = GaleriaBD.objects.get(pk=pk)
    ft.delete()
    return redirect('galeria')




