from django_filters import rest_framework as filters
from apis.models import Student, ClassRoom



class StudentFilter(filters.FilterSet):
    school_name = filters.CharFilter(method='school_filter', label="school_name")
    class_room = filters.ModelChoiceFilter(queryset=ClassRoom.objects.all())
    first_name = filters.CharFilter(lookup_expr='icontains')
    last_name = filters.CharFilter(lookup_expr='icontains')
    gender = filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Student
        fields = [ 'class_room', 'first_name', 'last_name', 'gender', 'school_name']
        
    def school_filter(self, queryset, name, value):
        if value is None:
            return Student.objects.none()
        return Student.objects.filter(class_room__school__name=value).distinct()
            
