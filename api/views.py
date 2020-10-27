from django.shortcuts import render

from django.core.exceptions import MultipleObjectsReturned
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from api.models import AthleteEvents, NocRegions
from api.serializers import AthleteEventsSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def athlete_events_basic(request):
    if request.method == 'GET':
        athlete_events = AthleteEvents.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            athlete_events = athlete_events.filter(title__icontains=title)
        athlete_events_serializer = AthleteEventsSerializer(athlete_events, many=True)
        return JsonResponse(athlete_events_serializer.data, safe=False)

    elif request.method == 'POST':
        athlete_events_data = JSONParser().parse(request)
        athlete_events_serializer = AthleteEventsSerializer(data=athlete_events_data)
        if athlete_events_serializer.is_valid():
            athlete_events_serializer.save()
            return JsonResponse(athlete_events_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(athlete_events_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = AthleteEvents.objects.all().delete()
        return JsonResponse({'message': f'{count[0]} Athlete Events were deleted from database!'}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
def athlete_events_itens(request, pk):
    try: 
        athlete_events = AthleteEvents.objects.get(pk=pk)
        if request.method == 'GET': 
            athlete_events_serializer = AthleteEventsSerializer(athlete_events)
            return JsonResponse(athlete_events_serializer.data)
        elif request.method == 'PUT': 
            athlete_events_data = JSONParser().parse(request) 
            athlete_events_serializer = AthleteEventsSerializer(athlete_events, data=athlete_events_data) 
            if athlete_events_serializer.is_valid(): 
                athlete_events_serializer.save() 
                return JsonResponse(athlete_events_serializer.data) 
            return JsonResponse(athlete_events_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE': 
            athlete_events.delete() 
            return JsonResponse({'message': 'The specified Athletic Event was deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
    except AthleteEvents.DoesNotExist: 
        return JsonResponse({'message': 'The Athlete Event does note exist on the database'}, status=status.HTTP_404_NOT_FOUND)
        
@api_view(['GET'])
def athlete_events_existent(request):
    athlete_events = AthleteEvents.objects.filter(published=True)
        
    if request.method == 'GET':
        athlete_events_serializer = AthleteEventsSerializer(athlete_events, many=True)
        return JsonResponse(athlete_events_serializer.data, safe=False)