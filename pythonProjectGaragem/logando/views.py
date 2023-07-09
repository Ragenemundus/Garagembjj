from django.contrib.auth.forms import AuthenticationForm
from django.contrib import  auth
from django.shortcuts import render, redirect


# Create your views here.
def logar_foto(request):
    form = AuthenticationForm(request)
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request,user)
            return redirect('galeria')


    return render(
        request,
        'logando.html',
        {
            'form': form
        }

    )
def deslogar(request):
    auth.logout(request)
    return redirect('galeria')