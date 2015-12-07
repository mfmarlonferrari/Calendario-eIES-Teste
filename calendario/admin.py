from django.contrib import admin
from calendario.models import *

# Register your models here.
admin.site.register(professor)
admin.site.register(disciplina)
admin.site.register(sala)
admin.site.register(aluno)
admin.site.register(turma)
admin.site.register(repeteDisciplina)