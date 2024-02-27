from rest_framework import serializers
from.models import Postal,PostalAddress

class postalserializer(serializers.ModelSerializer):
    class Meta:
        model = Postal
        fields = '__all__'

class postaladdressserializer(serializers.ModelSerializer):
    
    class Meta:
        model = PostalAddress
        fields = '__all__'
  
class PostalAddressListSerializer(serializers.ListSerializer):
    child = postaladdressserializer()