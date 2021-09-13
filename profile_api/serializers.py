from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    '''Serializes a nem field for testing out APIView'''
    name = serializers.CharField(max_length=10)
