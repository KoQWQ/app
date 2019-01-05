from rest_framework import serializers
from . models import Competition, Participant, Round


class CompetitionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Competition
        fields = '__all__'


class ParticipantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participant
        fields = '__all__'

class RoundSerializer(serializers.ModelSerializer):

    class Meta:
        model = Round
        fields = '__all__'