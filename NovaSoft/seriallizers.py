from rest_framework import serializers

from .models import Developer, Contact


class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    model = Contact
    fields = '__all__'