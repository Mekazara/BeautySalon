from django.shortcuts import render
from rest_framework import viewsets

from service.models import Master, Certificate, Service, Feedback
from service.serializers import MasterSerializer, CertificateSerializer, ServiceSerializer, FeedbackSerializer, \
    MasterCertificateList


class MasterViewset(viewsets.ModelViewSet):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer

class CertificateViewset(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

class ServiceViewset(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class FeedbackViewset(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer