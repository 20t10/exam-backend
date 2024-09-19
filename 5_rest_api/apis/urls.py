from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apis.views.v1.school import SchoolModelViewSet, ClassRoomModelViewSet
from apis.views.v1.teacher import TeacherModelViewSet
from apis.views.v1.student import StudentModelViewSet
router = DefaultRouter()
router.register(r'schools', SchoolModelViewSet, basename='school')
router.register(r'classrooms', ClassRoomModelViewSet, basename='classroom')
router.register(r'teachers', TeacherModelViewSet, basename='teacher')
router.register(r'students', StudentModelViewSet, basename='student')
api_v1_urls = (router.urls, 'v1')

urlpatterns = [
    path('v1/', include(api_v1_urls))
]
