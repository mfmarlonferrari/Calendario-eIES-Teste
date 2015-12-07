from django.db import models

class professor(models.Model):
    nomeProfessor = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nomeProfessor

class sala(models.Model):
    nomeSala = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nomeSala

class turma(models.Model):
    nomeTurma = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nomeTurma

class aluno(models.Model):
    nomeAluno = models.CharField(max_length=100)
    turma = models.ManyToManyField(turma)

    def __unicode__(self):
        return self.nomeAluno

class disciplina(models.Model):
    professor = models.ForeignKey(professor)
    sala = models.ForeignKey(sala)
    turma = models.ForeignKey(turma)
    horarioInicio = models.TimeField()
    horarioFinal = models.TimeField()
    nomeDisciplina = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nomeDisciplina

class repeteDisciplina(models.Model):
    qualDia = models.IntegerField()
    qualDisciplina = models.ForeignKey(disciplina)

