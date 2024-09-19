from django_filters import rest_framework as filters
from apis.models import School, ClassRoom
class SchoolFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = School
        fields = ['name']
        
class ClassRoomFilter(filters.FilterSet):
    school = filters.ModelChoiceFilter(queryset=School.objects.all())
    class Meta:
        model = ClassRoom
        fields = ['school']