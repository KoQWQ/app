from django.contrib import admin
from .models import Competition, Judge, Participant, Round, Entry


class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date',)
    list_filter = ('type', 'date',)
    search_fields = ('name',)


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'city',)
    list_filter = ('gender', 'payment',)
    search_fields = ('surname', 'name', 'city', 'school_name',)


class RoundAdmin(admin.ModelAdmin):
    list_display = ('name', 'competition',)
    list_filter = ('name', 'competition',)
    search_fields = ('participants',)


class EntryAdmin(admin.ModelAdmin):
    list_display = ('competition', 'round',)
    list_filter = ('competition', 'round',)


admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Judge)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Round, RoundAdmin)
admin.site.register(Entry, EntryAdmin)