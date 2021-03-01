from rest_framework import viewsets,generics
from school.models import Student, Subject, Registration
from school.serializer import StudentsSerializer, SubjectsSerializer, RegistrationsSerializer,ListRegistrationStudentSerializer,ListStudentsRegistrationsSerializer


class StudentsViewSet(viewsets.ModelViewSet):
    """Exibe todos os alunos"""
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer


class SubjectsViewSet(viewsets.ModelViewSet):
    """Exibe todos os cursos"""
    queryset = Subject.objects.all()
    serializer_class = SubjectsSerializer


class RegistrationsViewSet(viewsets.ModelViewSet):
    """Lista as Matriculas"""
    queryset = Registration.objects.all()
    serializer_class = RegistrationsSerializer


class ListRegistrationStudent(generics.ListAPIView):
    """Listando as matriculas de um aluno"""
    def get_queryset(self):
        queryset = Registration.objects.filter(aluno_id = self.kwargs['pk'])
        return queryset

    serializer_class = ListRegistrationStudentSerializer


class ListStudentsRegistration(generics.ListAPIView):
    """Listando alunos matriculados em um curso """

    def get_queryset(self):
        queryset = Registration.objects.filter(curso_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListStudentsRegistrationsSerializer
        

