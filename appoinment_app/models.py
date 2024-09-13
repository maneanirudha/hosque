from django.db import models

class appointmentData(models.Model):
    date = models.DateField()
    total_appointments = models.JSONField()
    current_token = models.IntegerField(default=0)