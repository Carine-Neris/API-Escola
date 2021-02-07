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
        fields = '__all__'
