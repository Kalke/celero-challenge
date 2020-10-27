from django.db import models


class AthleteEvents(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  
    name = models.TextField(db_column='Name', max_length=100)  
    sex = models.TextField(db_column='Sex')  
    age = models.IntegerField(db_column='Age', blank=True, null=True)  
    height = models.FloatField(db_column='Height', blank=True, null=True)  
    weight = models.FloatField(db_column='Weight', blank=True, null=True)  
    team = models.TextField(db_column='Team')  
    noc = models.TextField(db_column='NOC')  
    games = models.TextField(db_column='Games')  
    year = models.BigIntegerField(db_column='Year')  
    season = models.TextField(db_column='Season')  
    city = models.TextField(db_column='City')  
    sport = models.TextField(db_column='Sport')  
    event = models.TextField(db_column='Event')  
    medal = models.TextField(db_column='Medal',blank=True, null=True)  

    class Meta:
        db_table = 'athlete_events'

class NocRegions(models.Model):
    noc = models.TextField(db_column='NOC',primary_key=True, )  
    region = models.TextField()
    notes = models.TextField()

    class Meta:
        db_table = 'noc_regions'
