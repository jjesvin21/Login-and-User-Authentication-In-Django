from rest_framework import serializers
from django.contrib.auth.models import User
from loginapp.models import HasPermition

class UserSerialiser(serializers.ModelSerializer):
    haspermition = serializers.BooleanField()
    class Meta:
        model = User
        fields = ['username','password','email','first_name','last_name','haspermition']
    
    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        haspermition = validated_data['haspermition']

        user = User(username=username,email=email,first_name=first_name,last_name=last_name)
        user.set_password(password)
        user.save()
        permition = HasPermition(user=user,haspermition=haspermition)
        permition.save()
        return user

class PermitionSerializer(serializers.ModelSerializer):

    class Meta:
        model = HasPermition
        fields = '__all__'