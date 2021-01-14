from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Master(models.Model):
    name = models.CharField(max_length=50)
    expierence = models.IntegerField()
    photo = models.ImageField()
    service = models.ForeignKey(Service, on_delete=models.SET_NULL,
                                null=True, related_name='masters')

    def __str__(self):
        return self.name

class Certificate(models.Model):
    levels = (
        ('I level', 'I level'),
        ('II level', 'II level'),
        ('III level', 'III level')
    )
    name = models.CharField(max_length=50)
    date = models.DateField()
    location = models.CharField(max_length=50)
    level = models.CharField(max_length=30, choices=levels)
    master = models.ForeignKey(Master, on_delete=models.SET,
                               null=True, related_name='certificate')

    def __str__(self):
        return self.name


class Feedback(models.Model):
    author = models.CharField(max_length=40)
    text = models.TextField()
    service = models.ForeignKey(Service, on_delete=models.SET_NULL,
                                null=True, related_name='feedbacks')

    def __str__(self):
        return self.author + ' ' + self.service.name


