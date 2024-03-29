from django.shortcuts import render
from django.http import HttpResponse
from .utils import password_is_valid
from django.shortcuts  import redirect
from django.contrib.auth.models import User


def cadastro(request):

    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not password_is_valid(request, senha, confirmar_senha):
            return redirect ('/auth/cadastro')

        try:
            user = User.objects.create_user( username=username,
                                            password=senha,
                                            is_active=False)
            user.save()
            return redirect('/auth/logar')
        except:
            return HttpResponse('/auth/cadastro')


def logar(request):
    return HttpResponse("Voce esta na pagina de login")
