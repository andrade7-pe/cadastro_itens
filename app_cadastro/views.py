from django.shortcuts import render
from .models import Usuario

def prin(request):
    return render(request,'usuarios/prin.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    #Exibir usuarios em nova página
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    #Retornar os dados para a pagina
    return render(request,'usuarios/usuarios.html',usuarios)

    