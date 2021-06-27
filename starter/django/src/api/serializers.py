from rest_framework import serializers
from contacts.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    """Contact Serializer
    """
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'mobile', 'company', 'designation', 'notes']
        read_only_fields = ['id',]
