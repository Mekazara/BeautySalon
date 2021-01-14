from rest_framework import serializers

from service.models import Master, Certificate, Service, Feedback



class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['name', 'date', 'location', 'level']

class FeedbackSerializer(serializers.ModelSerializer):
    service = serializers.StringRelatedField()
    class Meta:
        model = Feedback
        fields = ['author', 'text', 'service']

class ServiceSerializer(serializers.ModelSerializer):
    feedbacks = FeedbackSerializer(many=True)
    class Meta:
        model = Service
        fields = ['name', 'description', 'price', 'masters', 'feedbacks']

class ServiceList(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['name', 'price']

class MasterCertificateList(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['name']

class MasterSerializer(serializers.ModelSerializer):
    certificate = MasterCertificateList(many=True)
    service = ServiceList()
    class Meta:
        model = Master
        fields = ['name', 'expierence', 'photo', 'certificate', 'service']

