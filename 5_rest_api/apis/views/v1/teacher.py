from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from apis.serializers import TeacherModelSerialzier, TeacherDetailModelSerialzier
from apis.models import Teacher
from apis.filters.teacher import TeacherFilter

class TeacherModelViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherModelSerialzier
    filter_backends = [DjangoFilterBackend]
    filterset_class = TeacherFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return TeacherModelSerialzier  
        if self.action == 'retrieve':
            return TeacherDetailModelSerialzier 
        return super().get_serializer_class()  
      