from rest_framework.serializers import ModelSerializer,SlugRelatedField
from .models import *
class AthleteSerializer(ModelSerializer):
    noc = SlugRelatedField(
        queryset= NOC.objects.all(),
        slug_field='noc'
     )
    class Meta:
        model = Athlete
        fields = ["id","name","sex","height","weight","noc"]

class NocSerializer(ModelSerializer):
    class Meta:
        model = NOC
        fields = "__all__"

class OlympicsSerializer(ModelSerializer):
    class Meta:
        model = Olympics
        fields = "__all__"

class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"

class SportSerializer(ModelSerializer):
    class Meta:
        model = Sport
        fields = "__all__"

class EventSerializer(ModelSerializer):
    sport = SlugRelatedField(
        queryset= Sport.objects.all(),
        slug_field='name'
     )
    class Meta:
        model = Event
        fields = "__all__"

class ParticipationSerializer(ModelSerializer):
    athlete = SlugRelatedField(
        queryset= Athlete.objects.all(),
        slug_field='name'
     )
    event = SlugRelatedField(
        queryset= Sport.objects.all(),
        slug_field='name'
     )
    city = SlugRelatedField(
        queryset= Sport.objects.all(),
        slug_field='name'
     )
    olympic = SlugRelatedField(
        queryset= Sport.objects.all(),
        slug_field='name'
     )

    class Meta:
        model = Participation
        fields = "__all__"

