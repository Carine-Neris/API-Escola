from rest_framework import serializers
from school.models import Student, Subject


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','nome','rg','cpf','data_nascimento']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
