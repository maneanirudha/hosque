from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http.response import JsonResponse

# Create your views here.

@api_view(['GET'])
def view_appoinment(request):
    return JsonResponse({"message":"Hello!"})

@api_view(['POST'])
def book_appoinment(request):
    return JsonResponse({'message':'Hello from POST API'})
