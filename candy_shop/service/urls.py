from django.urls import path, include
from rest_framework import routers
from service.views import MasterViewset, CertificateViewset, ServiceViewset, FeedbackViewset, OrderViewset, SignUp, \
    LoginView

router = routers.DefaultRouter()
router.register('master', MasterViewset, basename='master')
router.register('certificate', CertificateViewset, basename='certificate')
router.register('service', ServiceViewset, basename='service')
router.register('feedback', FeedbackViewset, basename='feedback')
router.register('order', OrderViewset, basename='order')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', SignUp.as_view()),
    path('login/', LoginView.as_view()),
]
