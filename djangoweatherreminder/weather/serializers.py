from rest_framework import serializers

from .models import CityName, CityWeather, UserSubscription


class CityNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityName
        fields = ['id', 'name', 'country', 'region', ]


class CityWeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityWeather
        fields = ['id', 'city', 'last_info_update', 'weather_description', 'temperature', 'feels_like',
                  'humidity', 'pressure', 'visibility', 'wind_speed', 'clouds', 'rain', 'snow', ]


class UserSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubscription
        fields = ['id', 'user', 'city', 'weather_info', 'notification_frequency', 'last_info_update', ]