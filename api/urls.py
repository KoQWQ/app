from django.conf.urls import url, include
from .views import CompetitionView, ParticipantView, RoundView, EntryView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'competitions', CompetitionView, base_name='competitions')
router.register(r'participants', ParticipantView, base_name='participants')
router.register(r'rounds', RoundView, base_name='rounds')
router.register(r'entries', EntryView, base_name='entries')

urlpatterns = [
    url(r'^', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]