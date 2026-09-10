from django.shortcuts import render


def inicio(request):
    return render(request, "tarefas/inicio.html")


def lista_tarefas(request):
    tarefas = [
        {
            "titulo": "Revisar requisitos do projeto",
            "prioridade": "Alta",
            "situacao": "Pendente",
        },
        {
            "titulo": "Criar estrutura inicial do Django",
            "prioridade": "Média",
            "situacao": "Concluída",
        },
    ]

    contexto = {"tarefas": tarefas}

    return render(request, "tarefas/lista.html", contexto)
