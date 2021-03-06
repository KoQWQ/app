from rest_framework import serializers
from . models import Competition, Participant, Round, Entry
from auth_user.models import UserAbstract
import datetime, time


class DisplayUser(serializers.ModelSerializer):
	class Meta:
		model = UserAbstract
		fields = '__all__'

	def to_representation(self, instance):
		data = {}
		data['id'] = instance.id
		data['full_name'] = '{} {}'.format(instance.surname, instance.name)
		return data


class CompetitionSerializer(serializers.ModelSerializer):
    display_participants = DisplayUser(many=True, read_only=True, source='participants')

    class Meta:
        model = Competition
        fields = ('name', 'type', 'date', 'cost', 'display_participants', 'participants', 'judges',)

    def to_representation(self, instance):
    	data = super(CompetitionSerializer, self).to_representation(instance)
    	data.update(date=time.mktime(instance.date.timetuple()) * 1000)
    	return data


class ParticipantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participant
        fields = '__all__'


class RoundSerializer(serializers.ModelSerializer):

    class Meta:
        model = Round
        fields = '__all__'


class EntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Entry
        fields = '__all__'