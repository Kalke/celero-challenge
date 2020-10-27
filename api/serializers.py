from rest_framework import serializers 
from api.models import AthleteEvents, NocRegions

class AthleteEventsSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = AthleteEvents
        fields = ('id',
                'name',
                'sex',
                'age',
                'height',
                'weight',
                'team',
                'noc',
                'games',
                'year',
                'season',
                'city',
                'sport',
                'event',
                'medal')

class NocRegionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = NocRegions
        fields = ('noc',
                'region',
                'notes')