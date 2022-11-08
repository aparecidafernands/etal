from django.shortcuts import render
from aluno.forms import AlunoForm


# Create your views here.

def cadastro_aluno(request):
    if request.method == 'POST':
        form =AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            form=AlunoForm()
    else:
        form = AlunoForm()
    return render (request, 'form.html', {'form' : form})