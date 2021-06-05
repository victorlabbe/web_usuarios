from django.contrib.auth import models
from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username","email")