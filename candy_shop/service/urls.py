
from django.urls import path, include
from rest_framework import routers

from service.views import MasterViewset, CertificateViewset, ServiceViewset, FeedbackViewset

router = routers.DefaultRouter()
router.register('master', MasterViewset, basename='master')
router.register('certificate', CertificateViewset, basename='certificate')
router.register('service', ServiceViewset, basename='service')
router.register('feedback', FeedbackViewset, basename='feedback')
urlpatterns = [
    path('', include(router.urls))
]
