from rest_framework import viewsets
from school.models import Student, Subject
from serializer import StudentSerializer, SubjectSerializer


class StudentsViewSet(viewsets.ModelViewSet):
    """Exibe todos os alunos"""
    queryset = Student.objects.all()]
    serializer_class = StudentSerializer


class SubjectsViewSet(viewsets.ModelViewSet):
    """Exibe todos os cursos"""
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
