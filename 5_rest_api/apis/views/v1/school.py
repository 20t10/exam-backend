from rest_framework import viewsets
from apis.models import School, ClassRoom
from apis.serializers import SchoolListModelSerializer, SchoolDetailModelSerialzier, ClassRoomListModelSerialzier, ClassRoomDetailModelSerialzier
from django_filters.rest_framework import DjangoFilterBackend
from apis.filters.school import SchoolFilter, ClassRoomFilter
class SchoolModelViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolListModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SchoolFilter
    
    def get_serializer_class(self):
        if self.action == 'list':
            return SchoolListModelSerializer  
        if self.action == 'retrieve':
            return SchoolDetailModelSerialzier 
        return super().get_serializer_class()  
      

class ClassRoomModelViewSet(viewsets.ModelViewSet):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomListModelSerialzier
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClassRoomFilter
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ClassRoomListModelSerialzier  
        if self.action == 'retrieve':
            return ClassRoomDetailModelSerialzier 
        return super().get_serializer_class()  
    
    