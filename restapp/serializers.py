from rest_framework import serializers
from .models import Student
from .models import Login

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'



class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=Login
        fields='__all__'