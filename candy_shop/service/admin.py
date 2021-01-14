from django.contrib import admin

from service.models import Feedback, Certificate, Service, Master

admin.site.register([Master, Certificate, Service, Feedback])
