from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'phone', 'email', 'message', 'created_date']

    def validate(self, attrs):
        name = attrs.get('name')
        message = attrs.get('message', None)
        if name and name.islower():
            raise ValidationError({"name": 'First letter of title must be uppercase'})
        if message and len(message) < 12:
            raise ValidationError({"message": 'Message must be grater than 12 digits'})
        return attrs
