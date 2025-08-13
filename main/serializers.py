from rest_framework import serializers
from .models import *

import datetime


# class ActorSerializer(serializers.Serializer):
#     id = serializers.IntegerField(required=False)
#     name = serializers.CharField()
#     country = serializers.CharField()
#     gender = serializers.CharField()
#     birth_date = serializers.DateField()

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

    def validate(self, data):
        error = False
        errors = ''
        if data.get('country').lower() == 'north korea' and data.get('gender').lower() == 'female':
            error = True
            errors = "Shimoliy Koreya ayol aktyorlari ushbu platformaga kirish huquqiga ega emas!"

        if data.get('birthdate') < datetime.date.today() - datetime.timedelta(weeks=5200):
            error = True
            errors += "Ushbu davrda tug'ilgan tirik aktyorlar mavjud emas!"
        if errors:
            raise serializers.ValidationError(errors)
        return data


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def validate_actors(self, actors):
        if len(actors) < 3:
            raise serializers.ValidationError(
                "Kamida 3 aktyor kiritishingiz kerak!"
            )
        return actors

    def validate_genre(self, value):
        if value.lower() in ['horror', 'retro']:
            raise serializers.ValidationError(
                "Ushbu janrdagi kinolar taqiqlanadi"
            )
        return value

    def validate_year(self, value):
        if int(value) < 1888:
            raise serializers.ValidationError(
                "Ushbu yilda filmlar mavjud emas!"
            )
        return value

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'



