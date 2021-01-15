from django.contrib.auth.models import User
from rest_framework import serializers
from service.models import Master, Certificate, Service, Feedback, Order


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['id', 'name', 'date', 'location', 'level']

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'author', 'text', 'service']

class ServiceSerializer(serializers.ModelSerializer):
    feedbacks = FeedbackSerializer(many=True)
    class Meta:
        model = Service
        fields = ['id', 'name', 'description', 'price', 'masters', 'feedbacks']

class ServiceList(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'price']

class MasterCertificateList(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['id', 'name']

class MasterSerializer(serializers.ModelSerializer):
    certificate = MasterCertificateList(many=True)
    service = ServiceList()
    class Meta:
        model = Master
        fields = ['id', 'name', 'expierence', 'photo', 'certificate', 'service']

class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Order
        fields = ['id', 'service', 'master', 'date', 'customer']

class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20, min_length=5)
    email = serializers.EmailField(allow_blank=False)
    password = serializers.CharField(max_length=16, min_length=8)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, **kwargs):
        user = User(username=self.validated_data['username'],
                    email=self.validated_data['email'])
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user

