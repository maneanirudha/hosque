from rest_framework import serializers
from .models import appointmentData

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = appointmentData
        fields = ['date', 'total_appointments']