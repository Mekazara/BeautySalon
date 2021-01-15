from django.contrib import admin

from service.models import Feedback, Certificate, Service, Master, Order

admin.site.register([Master, Certificate, Service, Feedback, Order])
