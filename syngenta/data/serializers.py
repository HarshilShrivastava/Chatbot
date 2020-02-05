from rest_framework import serializers
from .models import Data,query,DataHindi
class queryserializer(serializers.ModelSerializer):

    class Meta:
        model=query
        fields='__all__'
            
class answerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Data
        fields='__all__'
class answerhindiSerializer(serializers.ModelSerializer):
    class Meta:
        model=DataHindi
        fields=['ThreatName','WhyItOccurs','ProductName','Dosage']