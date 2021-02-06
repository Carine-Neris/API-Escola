from rest_framework import viewsets
from school.models import Student, Subject
from school.serializer import StudentsSerializer, SubjectsSerializer


class StudentsViewSet(viewsets.ModelViewSet):
    """Exibe todos os alunos"""
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer


class SubjectsViewSet(viewsets.ModelViewSet):
    """Exibe todos os cursos"""
    queryset = Subject.objects.all()
    serializer_class = SubjectsSerializer
