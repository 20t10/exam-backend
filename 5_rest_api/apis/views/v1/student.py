from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from apis.serializers import StudentModelSerialzier, StudentDetailModelSerialzier
from apis.models import Student
from apis.filters.student import StudentFilter

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerialzier
    filter_backends = [DjangoFilterBackend]
    filterset_class = StudentFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return StudentModelSerialzier  
        if self.action == 'retrieve':
            return StudentDetailModelSerialzier 
        return super().get_serializer_class()  
      