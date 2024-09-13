from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes, permission_classes
from django.http.response import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import appointmentData
from datetime import date
# Create your views here.

@api_view(['GET'])
@authentication_classes([TokenAuthentication])  # Use token authentication
@permission_classes([IsAuthenticated])
def view_appoinment(request):
    return JsonResponse({"message":"Hello!"})

@api_view(['POST'])
@authentication_classes([TokenAuthentication])  # Use token authentication
@permission_classes([IsAuthenticated])
def book_appoinment(request):
    user_id = request.user.id
    print(user_id)
    data = [{"user_id":user_id}]

    try:
        appointmentData.objects.get(date=date.today())
    except appointmentData.DoesNotExist:
        appointmentData.objects.create(date=date.today(),total_appointments=data)
        
    dat = appointmentData.objects.get(date=date.today())
    print(bool(dat))
    
    if dat:
        current_list = dat.total_appointments
        print(current_list)
        data.append(current_list)
        print(data)
        dat.total_appointments = data
        dat.save()
    else:
        pass

    # print(dat.total_appointments)
    return JsonResponse({'message':'Hello from POST API'})