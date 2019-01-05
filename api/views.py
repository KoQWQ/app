from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from . models import Competition, Participant, Round
from . serializers import CompetitionSerializer, ParticipantSerializer, RoundSerializer


class CompetitionView(viewsets.ModelViewSet):
    """
    retrieve:
    Получение одного конкурса из списка

    create:
    Создать новый конкурс

    list:
    Получить весь список конкурсов

    update:
    Изменить информацию о конкурсе

    partial_update:
    Изменить информацию о конкурсе

    delete:
    Удалить конкурс
    """
    permissions = (AllowAny,)
    serializer_class = CompetitionSerializer
    queryset = Competition.objects.all()


class ParticipantView(viewsets.ModelViewSet):
    """
    retrieve:
    Получение одного участника из списка

    create:
    Добавление участника

    list:
    Получить весь список участников

    update:
    Изменить информацию об участнике

    partial_update:
    Изменить информацию об участнике

    delete:
    Удалить участника
    """
    permissions = (AllowAny,)
    serializer_class = ParticipantSerializer
    queryset = Participant.objects.all()


class RoundView(viewsets.ModelViewSet):
    """
    retrieve:
    Получение одного раунда из списка

    create:
    Создать новый раунд

    list:
    Получить весь список раундов

    update:
    Изменить информацию о раунде

    partial_update:
    Изменить информацию о раунде

    delete:
    Удалить раунд
    """
    permissions = (AllowAny,)
    serializer_class = RoundSerializer
    queryset = Round.objects.all()