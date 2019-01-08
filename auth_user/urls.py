from django.urls import path
from .views import current_user, UserList

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view())
]
from rest_framework import routers
# urlpatterns = [
#     path('competitions', CompetitionView),
# ]

# router = routers.SimpleRouter()
# router.register(r'current_user', current_user)
# router.register(r'users', UserList.as_view())
# urlpatterns = router.urls