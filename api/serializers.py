from rest_framework import serializers
from . models import Competition, Participant, Round
from auth_user.models import UserAbstract

class DisplayUser(serializers.ModelSerializer):
	class Meta:
		model = UserAbstract
		fields = '__all__'

	def to_representation(self, instance):
		data = {}
		data['id'] = instance.id
		data['full_name'] = instance.get_full_name()
		return data

class CompetitionSerializer(serializers.ModelSerializer):
    display_participants = DisplayUser(many=True, read_only=True, source='participants')

    class Meta:
        model = Competition
        fields = ('name', 'type', 'date', 'cost', 'display_participants', 'participants',)


class ParticipantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participant
        fields = '__all__'


class RoundSerializer(serializers.ModelSerializer):

    class Meta:
        model = Round
        fields = '__all__'