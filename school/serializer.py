from rest_framework import serializers
from school.models import Student, Subject, Registration


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','nome','rg','cpf','data_nascimento']


class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class RegistrationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        exclude = []


class ListRegistrationStudentSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Registration
        fields = ['curso','periodo']

    def get_periodo(self,obj):
        return obj.get_periodo_display()


class ListStudentsRegistrationsSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model = Registration
        fields = ['aluno_nome']
