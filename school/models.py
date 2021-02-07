from django.db import models


class Student(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome


class Subject(models.Model):
    NIVEL = (
        ('B','Básico'),
        ('I','Intermediário'),
        ('A','Avançado')
    )
    
    codigo_curso = models.CharField(max_length=30)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default='B')


    def __str__(self):
        return self.descricao
    

class Registration(models.Model):
    PERIODO = (
    ('M','Matutino'),
    ('V', 'Vespertino'),
    ('N', 'Noturno')
    )

    aluno = models.ForeignKey(Student, on_delete = models.CASCADE)
    curso = models.ForeignKey(Subject, on_delete = models.CASCADE)
    periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False, default='M')
    


    
