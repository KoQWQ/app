from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from . models import Competition, Participant, Round, Entry
from . serializers import CompetitionSerializer, ParticipantSerializer, RoundSerializer, EntrySerializer


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
    filterset_fields = '__all__'
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
    filterset_fields = '__all__'
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
    filterset_fields = '__all__'
    queryset = Round.objects.all()


class EntryView(viewsets.ModelViewSet):
    """
    retrieve:
    Получение одного захода из списка

    create:
    Создать новый заход

    list:
    Получить весь список заходов

    update:
    Изменить информацию о заходе

    partial_update:
    Изменить информацию о заходе

    delete:
    Удалить заход
    """
    permissions = (AllowAny,)
    serializer_class = EntrySerializer
    filterset_fields = '__all__'
    queryset = Entry.objects.all()