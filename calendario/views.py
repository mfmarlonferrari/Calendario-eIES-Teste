from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
import json
from calendario.models import *

def cronograma(request, evento=None, id=None):
    lista = list()
    #carrega a lista com base no evento
    if evento=='professor':
        lista = professor.objects.all()
    elif evento=='sala':
        lista = sala.objects.all()
    elif evento=='disciplina':
        lista = disciplina.objects.all()
    elif evento=='turma':
        lista = turma.objects.all()
    elif evento=='aluno':
        lista = aluno.objects.all()
    context = dict(lista=lista, evento=evento, id=id)
    c = RequestContext(request, context)
    return render_to_response('cronograma.html', c)

def showCronograma(request, evento, pk):
    json_list = []
    if evento == 'professor':
        qualProfessor = professor.objects.get(id=pk)
        horarios = disciplina.objects.filter(professor=qualProfessor)
        for i in horarios:
            title = i.nomeDisciplina
            start = i.horarioInicio.strftime("%H:%M")
            end = i.horarioFinal.strftime("%H:%M")
            #cria a lista de repeticao do evento
            repeticao = repeteDisciplina.objects.filter(qualDisciplina=i)
            dow = list()
            for i in range(len(repeticao)):
                dow.append(repeticao[i].qualDia)
            json_entry = {'start': start, 'end': end, 'title': title, 'dow': dow}
            json_list.append(json_entry)
    elif evento == 'sala':
        qualSala = sala.objects.get(id=pk)
        horarios = disciplina.objects.filter(sala=qualSala)
        for i in horarios:
            title = i.nomeDisciplina
            start = i.horarioInicio.strftime("%H:%M")
            end = i.horarioFinal.strftime("%H:%M")
            #cria a lista de repeticao do evento
            repeticao = repeteDisciplina.objects.filter(qualDisciplina=i)
            dow = list()
            for i in range(len(repeticao)):
                dow.append(repeticao[i].qualDia)
            json_entry = {'start': start, 'end': end, 'title': title, 'dow': dow}
            json_list.append(json_entry)
    elif evento == 'disciplina':
        horarios = disciplina.objects.filter(id=pk)
        for i in horarios:
            title = i.nomeDisciplina
            start = i.horarioInicio.strftime("%H:%M")
            end = i.horarioFinal.strftime("%H:%M")
            #cria a lista de repeticao do evento
            repeticao = repeteDisciplina.objects.filter(qualDisciplina=i)
            dow = list()
            for i in range(len(repeticao)):
                dow.append(repeticao[i].qualDia)
            json_entry = {'start': start, 'end': end, 'title': title, 'dow': dow}
            json_list.append(json_entry)
    elif evento == 'turma':
        qualTurma = turma.objects.get(id=pk)
        horarios = disciplina.objects.filter(turma=qualTurma)
        for i in horarios:
            title = i.nomeDisciplina
            start = i.horarioInicio.strftime("%H:%M")
            end = i.horarioFinal.strftime("%H:%M")
            #cria a lista de repeticao do evento
            repeticao = repeteDisciplina.objects.filter(qualDisciplina=i)
            dow = list()
            for i in range(len(repeticao)):
                dow.append(repeticao[i].qualDia)
            json_entry = {'start': start, 'end': end, 'title': title, 'dow': dow}
            json_list.append(json_entry)
    elif evento == 'aluno':
        qualAluno = aluno.objects.get(id=pk)
        turmasDoAluno = qualAluno.turma.all()
        for t in turmasDoAluno:
            horarios = disciplina.objects.filter(turma=t)
            for i in horarios:
                title = i.nomeDisciplina
                start = i.horarioInicio.strftime("%H:%M")
                end = i.horarioFinal.strftime("%H:%M")
                #cria a lista de repeticao do evento
                repeticao = repeteDisciplina.objects.filter(qualDisciplina=i)
                dow = list()
                for i in range(len(repeticao)):
                    dow.append(repeticao[i].qualDia)
                json_entry = {'start': start, 'end': end, 'title': title, 'dow': dow}
                json_list.append(json_entry)
    return HttpResponse(json.dumps(json_list), content_type='application/json')