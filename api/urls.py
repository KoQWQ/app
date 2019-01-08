from django.conf.urls import url, include
from .views import CompetitionView, ParticipantView, RoundView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'competitions', CompetitionView)
router.register(r'participants', ParticipantView)
router.register(r'rounds', RoundView)

urlpatterns = [
    url(r'^', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]