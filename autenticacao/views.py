from django.shortcuts import render
from django.http import HttpResponse


def cadastro(request):

    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        return HttpResponse("Testando")


def logar(request):
    return HttpResponse("teste 2")
