from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from  rest_framework.views import APIView
from rest_framework.response import Response
from .models import Login
from .serializers import LoginSerializer
from django.shortcuts import get_list_or_404

# Create your views here.


class StudentList(APIView):
    def get(self,request):
        studentlist1=Student.objects.all()
        serializer=StudentSerializer(studentlist1,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
class LoginList(APIView):
    def get(self,request):
        loginlist1=Login.objects.all()
        serializer=LoginSerializer(loginlist1,many=True)
        return Response(serializer.data)
    def post(self,request):
         serializer=LoginSerializer(data=request.data)
         if serializer.is_valid():
             return Response(serializer.data,status=status.HTTP_201_CREATED)
         else:
             return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)







