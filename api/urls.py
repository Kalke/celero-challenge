from django.conf.urls import url 
from api import views 
 
urlpatterns = [ 
    url(r'^api/challenge$', views.athlete_events_basic),
    url(r'^api/challenge/(?P<pk>[0-9]+)$', views.athlete_events_itens),
    url(r'^api/challenge/published$', views.athlete_events_existent)
]