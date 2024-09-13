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
    """
    body :
    {
  "username": "newuser",
  "first_name": "John",
  "last_name": "Doe",
  "email": "johndoe@example.com",
  "password": "password123",
  "mobile_number": "1234567890"
    }   

    
    """
    user_id = request.user.id
    print(user_id)
    data = {"user_id":user_id}

    try:
        appointmentData.objects.get(date=date.today())
    except appointmentData.DoesNotExist:
        appointmentData.objects.create(date=date.today(),total_appointments=[{"user_id":user_id,"token_number":1}],current_token=1)
        return JsonResponse({'message':'Appoinment booked successfully!','token_number':1})
        
    dat = appointmentData.objects.get(date=date.today())
    print(bool(dat))
    
    if dat and dat.current_token != 4:
        current_list = dat.total_appointments
        print(current_list)
        user_list = [user['user_id'] for user in current_list]
        print(user_list)
        if user_id not in user_list:
            token_num = dat.current_token+1
            current_list.append({"user_id":user_id,"token_number":token_num})
            dat.current_token+=1
            print(current_list)
            # Use a list comprehension with a helper set to remove duplicates
            seen = set()
            unique_list = []
            for d in current_list:
                # Convert dictionary to a frozenset of items for immutability
                item = frozenset(d.items())
                if item not in seen:
                    seen.add(item)
                    unique_list.append(d)

            print(unique_list)

            dat.total_appointments = unique_list
            dat.save()
            return JsonResponse({'message':'Appoinment booked successfully!','token_number':token_num})
        else:
            return JsonResponse({'message':'You have already booked the appointment!'})
    else:
        return JsonResponse({'message':'today quota is over!'})
