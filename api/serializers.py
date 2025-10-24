from rest_framework import serializers


class EmailSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=255)
    body = serializers.CharField()
    email = serializers.EmailField()
