from django.shortcuts import render
from rest_framework.views import APIView
from loginapp.serializer import UserSerialiser
from rest_framework.response import Response

from loginapp.models import HasPermition
from loginapp.serializer import PermitionSerializer

# imports for authentication
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

# Create your views here.


# Custom permition class for Cheking wether the loginded user has the acess to the operation

class Permition_Authentication(permissions.BasePermission):
    
    def has_permission(self, request, view):

        user = request.user
        quriset = HasPermition.objects.get(user=user)
        serializer = PermitionSerializer(quriset)
        data = serializer.data
        if data['haspermition'] == True:
            return True
        else:
            return False

        
# For creating a new user 

class CreateUser(APIView):


    def post(self,request):
        data = request.data
        serializer = UserSerialiser(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"User added......"})
        return Response(serializer.errors)

# Only the the outhenticated useres [ useres with haspermition = true in HasPermition Table are allowed to acess this class]
    
class Hello(APIView):
    permission_classes = [IsAuthenticated,Permition_Authentication]

    def get(self,request):
        return Response({"msg":"Hello ........"})
        


