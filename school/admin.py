from django.contrib import admin
from school.models import Student, Subject


class Students(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id','nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Student,Students)


class Subjects(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao')
    list_display_links = ('id','codigo_curso')
    search_fields = ('codigo_curso',)

admin.site.register(Subject, Subjects)


