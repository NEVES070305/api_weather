
from rest_framework import serializers

class WeatherSerializer(serializers.Serializer):
    temperature = serializers.FloatField()
    date = serializers.DateTimeField()
    city = serializers.CharField(max_length=255, allow_blank=True)
    atmosphericPressure = serializers.FloatField(required=False)
    humidity = serializers.FloatField(required=False)
    weather = serializers.CharField(max_length=255, allow_blank=True)